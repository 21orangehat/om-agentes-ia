# Módulo 1, Aula 2
from agents import Agent, Runner, RunResult

from helper import get_agent

def main() -> None:
    agent: Agent = get_agent(
        name="Agente Principal",
        instructions='Você é um assistente prestativo. Seja direto ao ponto.' # system_prompt
    )

    result: RunResult = Runner.run_sync(
        starting_agent=agent,
        input='Escreva-me um poema sobre python'
    )

    print(result.final_output)


if __name__ == '__main__':
    main()
