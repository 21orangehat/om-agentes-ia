import os
import subprocess
import httpx
from random import randint
from datetime import datetime
from typing import List
from agents import Agent, function_tool, RunContextWrapper

from models import UserInfo, Cliente, Compra


@function_tool
async def get_weather(location: str) -> str:
    """
    Função que recebe uma localização via parâmetro,
    busca e retorna a temperatura e condições climáticas
    na API da WeatherAPI.com 
    """
    url: str = "https://api.weatherapi.com/v1/current.json"
    params: dict[str,str] = {
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
    Executa um comando de terminal usando um shell e captura sua saída.

    Esta função utiliza `subprocess.run` com `shell=True`, `stdout=subprocess.PIPE`,
    e `stdin=subprocess.PIPE` para executar o comando fornecido.
    A saída padrão e o erro padrão são capturados e o stdin é configurado para ser
    um pipe, mas nenhuma entrada é enviada por padrão.

    Args:
        arg: A string de comando do terminal a ser executada (e.g., "ls -l" ou "echo 'hello'").

    Returns:
        Um objeto subprocess.CompletedProcess. Os atributos importantes
        são:
        - .stdout: A saída padrão do comando (em bytes).
        - .stderr: O erro padrão do comando (em bytes).
        - .returncode: O código de saída do comando (0 para sucesso na maioria das vezes).

    Raises:
        Qualquer exceção que subprocess.run possa levantar (e.g., FileNotFoundError,
        TimeoutError, ou CalledProcessError se 'check=True' fosse usado).

    Examples:
        >>> import subprocess
        >>> result = terminal_command("echo 'Teste de comando'")
        >>> result.returncode
        0
        >>> result.stdout.decode().strip()
        'Teste de comando'

        >>> result_fail = terminal_command("comando_inexistente_xyz")
        >>> result_fail.returncode != 0
        True
        # A saída de erro estaria em result_fail.stderr
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

    purchase_list = '. '.join([f"{c.produto.nome} US$({c.produto.preco:.2f})" for c in compras])

    return f"Compras: {purchase_list}"

@function_tool
def get_client_info(wrapper: RunContextWrapper[Cliente]) -> str:
    """
    Função que retorna informações de um cliente.
    """
    return f"ID Cliente: {wrapper.context.id}\nCliente: {wrapper.context.nome}"


@function_tool
def get_number():
    """
    Função para retornar um número inteiro, pseudo-alattório,
    entre 1 e 20.
    """
    n = randint(1, 20)
    return n


def dynamic_client_instructions(wrapper: RunContextWrapper[Cliente], agent: Agent[Cliente]) -> str:
    """
    Função para gerar instruções dinâmicas de acordo com o cliente.
    """
    novo: bool = wrapper.context.novo

    if novo:
        return f"Você é um assistente de suporte. O usuário chama-se {wrapper.context.nome} e ele é novo na plataforma. Explique tudo com calma, de maneira detalhada e amivável. Seja paciente e muito didático."
    return f"Você é um assistente de suporte experiente e direto. O usuário chama-se {wrapper.context.nome} e já é nosso cliente antigo da plataforma. Responsa a ele de forma clara e direta, sem enrolação mas sempre com educação."

