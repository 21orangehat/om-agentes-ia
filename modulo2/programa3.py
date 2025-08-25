from agents import Agent, Runner, RunResult

from core.helpers import (
    get_agent, 
    get_weather,
    terminal_command,
)

mensagens = [
    {
        "role": "system",
        "content": "Você é um assistente. Responda sempre em português do Brasil e de forma muito formal.",
    }
]

def main() -> None:
    agente: Agente = get_agent(
        name="Agente Geral",
        tools=[get_weather, terminal_command]
    )

    while True:
        user_imput = input("User: ")
        print("\n")

        if user_imput == "sair":
            print("Chat finalizado...")
            break

        mensagens.append({"role": "user", "content": user_imput})

        result: RunResult = Runner.run_sync(
            starting_agent=agente, 
            input=mensagens
        )
        print(f"Assistant: {result.final_output}\n")

        mensagens.append({"role": "assistant", "content": result.final_output})

"""

"""
