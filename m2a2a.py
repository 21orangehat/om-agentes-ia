# Módulo 2, Aula 2
from agents import Agent, Runner, RunResult

from helper import get_agent
from tools import get_weather, get_current_time, terminal_command

def main() -> None:
    agent: Agent = get_agent(
        name="Agente Geral",
        instructions='Você é um assistente. Responsa sempre em português e de forma muito formal.', # system_prompt
        tools=[get_weather, get_current_time, terminal_command]
    )

    result: RunResult = Runner.run_sync(
        starting_agent=agent,
        input='O que você é capaz de fazer?'
    )

    print(result.final_output)


if __name__ == '__main__':
    main()
