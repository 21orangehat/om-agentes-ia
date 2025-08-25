from agents import Agent, Runner, RunResult, SQLiteSession

from core.helpers import (
    get_agent,
    get_session,
    get_weather,
    terminal_command,
)

def main() -> None:
    agente: Agente = get_agent(
        name="Agente Geral",
        instructions="Você é um assistente. Responda sempre em português do Brasil e de forma muito formal.",
        tools=[get_weather, terminal_command]
    )
    session: SQLiteSession = get_session(session_id="chat_1")

    while True:
        try:
            user_imput = input("User: ")
            print("\n")

            if user_imput == "sair":
                print("Chat finalizado...")
                session.close()
                break

            result: RunResult = Runner.run_sync(
                starting_agent=agente, 
                input=user_imput,
                session=session
            )
            print(f"Assistant: {result.final_output}\n")
        except KeyboardInterrupt as e:
            session.close()
            break

"""

"""
