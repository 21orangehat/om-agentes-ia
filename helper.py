import os
from typing import List
from agents import (
    Agent, 
    OpenAIChatCompletionsModel, 
    AsyncOpenAI,
    SQLiteSession,
    set_tracing_disabled,
)
from dotenv import load_dotenv
load_dotenv()
set_tracing_disabled(disabled=True)

def get_model() -> OpenAIChatCompletionsModel:
    """
    Função que instancia e retorna um OpenAIChatCompletionsModel.

    Testes usando o LM Studio

    Com o model qwen/qwq-32b, ficou muito lento...

    Com o model qwen/qwen3-4b-thinking-2507:2, ficou muito lento...

    Com o model openai/gpt-oss-20b, ficou bom...

    Com o model mistralai/magistral-small-2509, ficou bom...
    """
    model: OpenAIChatCompletionsModel = OpenAIChatCompletionsModel(
        model='mistralai/magistral-small-2509',
        openai_client=AsyncOpenAI(
            api_key=os.environ.get('OPENAI_API_KEY'), 
            base_url="http://127.0.0.1:1234/v1",
        )
    )

    return model


def get_agent(name: str, instructions: str = None, tools: List[any]=[]) -> Agent:
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
    """
    É via session_id que a LLM guarda o contexto das conversas.
    """
    session: SQLiteSession = SQLiteSession(session_id=session_id, db_path=db_path)

    return session
