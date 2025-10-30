# Módulo 3, Aula 1
from agents import Agent, Runner, RunResult

from helper import get_agent
from tools import fetch_user_info

from models import UserInfo

def main() -> None:
    agent: Agent = get_agent(
        name="Agente de Suporte da Empresa",
        instructions='Você é responsável por ajudar nossos funcionários com as suas solicitações.',
        tools=[fetch_user_info,]
    )

    user_info: UserInfo = UserInfo(nome="Orange Hat", cargo="Desenvolvedor Pleno")

    while True:
        try:
            user_input = input("User: ")
            print('\n')

            if user_input == 'sair':
                print("Chat finalizado...")
                break
        
            result: RunResult = Runner.run_sync(starting_agent=agent, input=user_input, context=user_info)
            print(f"Assistant: {result.final_output}\n")
        except KeyboardInterrupt as e:
            break


if __name__ == '__main__':
    main()
