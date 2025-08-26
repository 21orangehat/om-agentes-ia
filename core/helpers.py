import os
import subprocess
import httpx
from datetime import datetime
from typing import List
from agents import (
    Agent, 
    OpenAIChatCompletionsModel, 
    AsyncOpenAI, 
    function_tool,
    SQLiteSession,
    RunContextWrapper
)
from dotenv import load_dotenv

from core.models import UserInfo, Cliente, Compra

load_dotenv()

# Agents Base

def get_model() -> OpenAIChatCompletionsModel:
    """
    Função que instancia e retorna um OpenAIChatCompletionsModel.
    """
    model: OpenAIChatCompletionsModel = OpenAIChatCompletionsModel(
        model='gemini-2.0-flash',
        openai_client=AsyncOpenAI(
            api_key=os.environ.get('GOOGLE_AI_KEY'), 
            base_url="https://generativelanguage.googleapis.com/v1beta",
        )
    )

    return model


def get_agent(name: str, instructions: str = None, tools: list[any]=[]) -> Agent:
    """
    Função que instancia e retorna um Agent baseado
    no nome, instruções e tools recebidas via parâmetro.
    """
    agente: Agent = Agent(
        name=name,
        instructions=instructions,
        model=get_model(),
        tools=tools
    )

    return agente


def get_session(session_id: str, db_path="session.db"):
    session = SQLiteSession(session_id=session_id, db_path=db_path)

    return session


# Tools

@function_tool
async def get_weather(location: str) -> str:
    """
    Função que recebe uma localização via parâmetro,
    busca e retorna a temperatura e condições climáticas
    na API da WeatherAPI.com 
    """
    url = "https://api.weatherapi.com/v1/current.json"
    params = {
        "key": os.environ.get('WEATHER_API_KEY'),
        "q": location,
        "lang": "pt"
    }
    
    async with httpx.AsyncClient() as client:
        try:
            r = await client.get(url=url, params=params)
            r.raise_for_status()
            data = r.json()
            temp = data['current']['temp_c']
            condition = data['current']['condition']['text']

            return f"Em {location}, a temperatura está {temp} e as condições {condition}"
        except Exception as e:
            return f"Não foi possível fazer a requisição para {location} : {e}"


@function_tool
def get_current_time() -> datetime:
    """
    Função que returna a hora atual.
    """
    return datetime.now()

@function_tool
def terminal_command(arg: str):
    """
    Função que insere um comando de terminal e mostra a saída.
    """
    return subprocess.run(
        arg, shell=True, 
        stdout=subprocess.PIPE, 
        stdin=subprocess.PIPE
    )


@function_tool
def fetch_user_info(wrapper: RunContextWrapper[UserInfo]) -> str:
    """
    Função que busca informações dos nossos funcionários.
    """
    return f"O nome do deste funcionário é {wrapper.context.nome} e seu cargo é {wrapper.context.cargo}"


@function_tool
def update_user_info(wrapper: RunContextWrapper[UserInfo], nome: str, cargo: str) -> str:
    """
    Função que atuaiza informações dos nossos funcionários.
    """
    wrapper.context.nome = nome
    wrapper.context.cargo = cargo
    return "Informações atualizadas com sucesso."


@function_tool
def get_client_recent_purchases(wrapper: RunContextWrapper[Cliente], n: int) -> str:
    """
    Função que retorna as 3 últimas compras de um cliente.
    """
    compras: List[Compra] = wrapper.context.get_recent_purchases(n)

    purchase_list = '. '.join([f"{c.produto} US$({c.preco:.2f})" for c in compras])

    return f"Compras: {purchase_list}"

@function_tool
def get_client_info(wrapper: RunContextWrapper[Cliente]) -> str:
    """
    Função que retorna informações de um cliente.
    """
    return f"ID Cliente: {wrapper.context.id}\nCliente: {wrapper.context.nome}"


if __name__ == '__main__':
    import asyncio
    ret = asyncio.run(get_weather(location='São Paulo'))
    print(ret)
