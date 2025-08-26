from agents import (
    Agent, 
    Runner, 
    RunResult
)

from core.helpers import (
    get_agent,
    get_session,
    get_weather,
    terminal_command,
    fetch_user_info
)

from core.models import UserInfo


def main() -> None:
    user_info: UserInfo = UserInfo(nome="Orange Hat", cargo="Desenvolvedor Pleno")

    agente_de_suporte: Agente = get_agent(
        name="Agente de Suporte da Empresa",
        instructions="Você é responsável por ajudar nossos funcionários com as solicitações deles.",
        tools=[fetch_user_info,]
    )

    result: RunResult = Runner.run_sync(
        starting_agent=agente_de_suporte, 
        input="Olá, qual é o meu nome?",
        context=user_info
    )
    
    print(f"Assistant: {result.final_output}\n")

"""

"""
