# Módulo 2, Aula 2
from typing import List
from agents import Agent, Runner, RunResult

from helper import get_agent
from tools import get_weather, get_current_time, terminal_command

def main() -> None:
    agent: Agent = get_agent(
        name="Agente Geral",
        tools=[get_weather, get_current_time, terminal_command]
    )

    mensagens: List[dict[str,str]] = [
        {"role": "system", "content": "Você é um assistente. Responsa sempre em português e de forma muito formal. Cuidado com arquivos contendo conteúdo sensível."}
    ]
    
    while True:
        user_input = input("User: ")
        print('\n')

        if user_input == 'sair':
            print("Chat finalizado...")
            break

        mensagens.append({"role": "user", "content": user_input})
        
        result: RunResult = Runner.run_sync(starting_agent=agent, input=mensagens)

        print(f"Assistant: {result.final_output}\n")

        mensagens.append({"role": "assistant", "content": result.final_output})


if __name__ == '__main__':
    main()
