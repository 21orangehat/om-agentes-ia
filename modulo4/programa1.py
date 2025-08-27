from agents import (
    Agent, 
    Runner, 
    RunResult,
    RunContextWrapper
)

from core.helpers import get_agent, terminal_command


def main() -> None:
    
    assistant: Agent = get_agent(
        name="Assistant",
        tools=[terminal_command,]
    )

    while True:
        
        try:
            user_input: str = input('User: ')
            print('\n')

            if user_input == "sair":
                print("Fechando o chat...")
                break

            result: RunResult = Runner.run_sync(
                starting_agent=assistant, 
                input=user_input
            )
    
            print(f"Assistant: {result.final_output}\n")
        except KeyboardInterrupt as e:
            break
