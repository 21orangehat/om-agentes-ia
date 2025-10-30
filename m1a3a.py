# Módulo 1, Aula 3
from agents import Agent, Runner, RunResult

from helper import get_agent
from tools import get_weather

def main() -> None:
    agent: Agent = get_agent(
        name="Agente de Previsão do Tempo",
        instructions='Você é um agente de previsão do tempo. Responsa sempre em português e de forma informal.', # system_prompt
        tools=[get_weather,]
    )

    result: RunResult = Runner.run_sync(
        starting_agent=agent,
        input='Como está o clima em Braga?'
    )

    print(result.final_output)


if __name__ == '__main__':
    main()
