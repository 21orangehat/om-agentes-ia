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

            result: RunResultStreaming = Runner.run_streamed(
                starting_agent=assistant, 
                input=user_input,
                session=session,
                max_turns=33
            )
            
            print('Assistant: ', end='')
            async for event in result.stream_events():
                if event.type == 'raw_response_event' and isinstance(event.data, ResponseTextDeltaEvent):
                    print(event.data.delta, end='', flush=True)
            print('\n')
        except KeyboardInterrupt as e:
            session.close()
            break
        except MaxTurnsExceeded as f:
            print('Excedeu o número de execuções...')

"""
Continuo tendo, as vezes, o erro: [non-fatal] Tracing: server error 500, retrying.
mas o programa não crasha, continua funcionando normalmente.

Agora tive novo erro:
openai.RateLimitError: Error code: 429 - [{'error': {'code': 429, 'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits.', 'status': 'RESOURCE_EXHAUSTED', 'details': [{'@type': 'type.googleapis.com/google.rpc.QuotaFailure', 'violations': [{'quotaMetric': 'generativelanguage.googleapis.com/generate_content_free_tier_requests', 'quotaId': 'GenerateRequestsPerMinutePerProjectPerModel-FreeTier', 'quotaDimensions': {'location': 'global', 'model': 'gemini-2.0-flash'}, 'quotaValue': '15'}]}, {'@type': 'type.googleapis.com/google.rpc.Help', 'links': [{'description': 'Learn more about Gemini API quotas', 'url': 'https://ai.google.dev/gemini-api/docs/rate-limits'}]}, {'@type': 'type.googleapis.com/google.rpc.RetryInfo', 'retryDelay': '33s'}]}}]

Aparentemente atingi o limite de uso do Google Gemini...
"""
