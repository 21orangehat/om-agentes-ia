from agents import Agent, Runner, RunResult

from core.helpers import get_agent, get_weather, get_current_time

def main() -> None:
    agente: Agente = get_agent(
        name="Agente de Previsão do Tempo",
        instructions="Você é um agente de previsão do tempo. Responda sempre em português do Brasil e de forma muito formal.",
        tools=[get_weather, get_current_time]
    )

    result: RunResult = Runner.run_sync(
        starting_agent=agente, 
        input="Que horas são agora e como está o clima em Braga?"
    )

    print(result.final_output)
