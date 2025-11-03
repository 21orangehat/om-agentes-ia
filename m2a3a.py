# Módulo 2, Aula 3
from agents import Agent, Runner, RunResult, SQLiteSession

from helper import get_agent, get_session
from tools import get_weather, get_current_time, terminal_command

def main() -> None:
    agent: Agent = get_agent(
        name="Agente Geral",
        instructions='Você é um assistente. Responsa sempre em português e de forma muito formal. Cuidado com arquivos contendo conteúdo sensível.',
        tools=[get_weather, get_current_time, terminal_command]
    )

    session: SQLiteSession = get_session('chat_1')

    while True:
        try:
            user_input = input("User: ")
            print('\n')

            if user_input == 'sair':
                print("Chat finalizado...")
                session.close()
                break
        
            result: RunResult = Runner.run_sync(starting_agent=agent, input=user_input, session=session)
            print(f"Assistant: {result.final_output}\n")
        except KeyboardInterrupt as e:
            session.close()
            break


if __name__ == '__main__':
    main()
