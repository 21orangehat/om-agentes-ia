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
    fetch_user_info,
    update_user_info
)

from core.models import UserInfo


def main() -> None:
    user_info: UserInfo = UserInfo(nome="Orange Hat", cargo="Desenvolvedor Pleno")

    session: SQLiteSession = get_session(session_id="m3chat_1") 

    agente_de_suporte: Agent = get_agent(
        name="Agente de Suporte da Empresa",
        instructions="Você é responsável por ajudar nossos funcionários com as solicitações deles.Se um funcionário questionar que alguma informação sobre ele está errada, atualize as informações com a tool update_user_info",
        tools=[fetch_user_info, update_user_info]
    )

    while True:
        
        try:
            user_input: str = input('User: ')
            print('\n')

            if user_input == "sair":
                print("Fechando o chat...")
                session.close()
                break

            result: RunResult = Runner.run_sync(
                starting_agent=agente_de_suporte, 
                input=user_input,
                context=user_info,
                session=session
            )
    
            print(f"Assistant: {result.final_output}\n")
        except KeyboardInterrupt as e:
            session.close()
            break

"""

"""
