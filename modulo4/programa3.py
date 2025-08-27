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
                session.close()
                break

            result: RunResultStreaming = Runner.run_streamed(
                starting_agent=assistant, 
                input=user_input,
                session=session
            )
            
            print('Assistant: ', end='')
            async for event in result.stream_events():
                if event.type == 'raw_response_event' and isinstance(event.data, ResponseTextDeltaEvent):
                    print(event.data.delta, end='', flush=True)
            print('\n')
        except KeyboardInterrupt as e:
            session.close()
            break

"""
Utilizando o Gemini do Google, praticamente nunca ele executa os comandos
de terminal sem que eu tenha que avisar a ele que ele tem acesso à tool
e que deve executar os comandos necessários.

Ao solicitar para ele verificar se o Django estava instalado, ao invés de executar
o comando ele me apresentou o comando que eu deveria executar para verificar isso.

Depois deu dizer a ele que ele tem acesso ao terminal e que conhece o comando para
fazer isso, então que faça. Ele fez e disse que o Django não estava instalado.

Solicitei a ele que instalasse o Django, ele instalou.

Solicitei a ele que criasse um projeto Django chamado meu_app e ele criou.

Solicitei a ele que criasse, dentro do projeto meu_app uma aplicação chamada
core contendo um arquivo helper.py e então a aplicação crashou com o erro:

openai.BadRequestError: Error code: 400 - [{'error': {'code': 400, 'message': 'Request contains an invalid argument.', 'status': 'INVALID_ARGUMENT'}}]
"""