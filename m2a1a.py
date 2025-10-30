# Módulo 2, Aula 1
from agents import Agent, Runner, RunResult

from helper import get_agent
from tools import get_weather, get_current_time

def main() -> None:
    agent: Agent = get_agent(
        name="Agente de Previsão do Tempo",
        instructions='Você é um agente de previsão do tempo. Responsa sempre em português e de forma muito formal.', # system_prompt
        tools=[get_weather]
    )

    result: RunResult = Runner.run_sync(
        starting_agent=agent,
        input='Como está o clima em Braga? E que horas são agora?'
    )

    print(result.final_output)


if __name__ == '__main__':
    main()
