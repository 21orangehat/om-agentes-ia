import asyncio

from agents import (
    Agent, 
    Runner, 
    RunResultStreaming,
    RunContextWrapper,
    SQLiteSession,
    MaxTurnsExceeded
)
from openai.types.responses import ResponseTextDeltaEvent

from core.helpers import get_agent, get_session, get_number


async def main() -> None:

    session: SQLiteSession = get_session(session_id="m4chat_2") 
    
    assistant: Agent = get_agent(
        name="Assistant",
        tools=[get_number,]
    )

    while True:
        
        try:
            user_input: str = input('User: ')
            print('\n')

            if user_input == "sair":
                print("Fechando o chat...")
                session.close()
                break

            result: RunResultStreaming = await Runner.run(
                starting_agent=assistant, 
                input=user_input,
                session=session,
                max_turns=3
            )
            
            print(f'Assistant: {result.final_output}')
        except KeyboardInterrupt as e:
            session.close()
            break
        except MaxTurnsExceeded as f:
            print('Excedeu o número de execuções...')

"""

"""
