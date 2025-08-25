import os
import httpx
from datetime import datetime
from agents import Agent, OpenAIChatCompletionsModel, AsyncOpenAI, function_tool
from dotenv import load_dotenv

load_dotenv()


@function_tool
async def get_weather(location: str) -> str:
    """
    https://www.weatherapi.com/
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
        except:
            return f"Não foi possível fazer a requisição para {location}"


@function_tool
def get_current_time() -> datetime:
    return datetime.now()


def get_model() -> OpenAIChatCompletionsModel:
    model: OpenAIChatCompletionsModel = OpenAIChatCompletionsModel(
        model='gemini-2.0-flash',
        openai_client=AsyncOpenAI(
            api_key=os.environ.get('GOOGLE_AI_KEY'), 
            base_url="https://generativelanguage.googleapis.com/v1beta",
        )
    )

    return model


def get_agent(name: str, instructions: str, tools: list[any]=[]) -> Agent:
    agente: Agent = Agent(
        name=name,
        instructions=instructions,
        model=get_model(),
        tools=tools
    )

    return agente
