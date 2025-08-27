import asyncio

"""
https://openai.github.io/openai-agents-python/streaming/
"""

from agents import (
    Agent, 
    Runner, 
    RunResultStreaming,
    RunContextWrapper,
    SQLiteSession
)
from openai.types.responses import ResponseTextDeltaEvent

from core.helpers import get_agent, get_session, terminal_command


async def main() -> None:

    session: SQLiteSession = get_session(session_id="m4chat_1") 
    
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

            result: RunResultStreaming = Runner.run_streamed(
                starting_agent=assistant, 
                input=user_input
            )
    
            async for event in result.stream_events():
                if event.type == 'raw_response_event' and isinstance(event.data, ResponseTextDeltaEvent):
                    print(event.data.delta, end='', flush=True)
        except KeyboardInterrupt as e:
            break
