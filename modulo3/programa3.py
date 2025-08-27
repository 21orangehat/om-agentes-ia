from uuid import uuid4

from agents import (
    Agent, 
    Runner, 
    RunResult,
    SQLiteSession
)

from core.helpers import (
    get_agent,
    get_session,
    get_weather,
    get_client_recent_purchases,
    get_client_info
)

from core.models import Cliente, Compra


def main() -> None:
    client: Cliente = Cliente(
        id=uuid4().__str__(),
        nome='Ray Sychev',
        compras=[
            Compra(id=uuid4().__str__(), produto="PlayStation 5", preco=499.99),
            Compra(id=uuid4().__str__(), produto="Silent Hill 2", preco=67.34),
            Compra(id=uuid4().__str__(), produto="Candy", preco=9.00),
            Compra(id=uuid4().__str__(), produto="Pendrive 32GB", preco=29.26),
        ]
    )

    session: SQLiteSession = get_session(session_id="m3chat_2") 

    agente_de_atendimento: Agent = get_agent(
        name="Agente de Suporte da Empresa",
        instructions="Você é um assistente inteligente que ajuda clientes com dúvidas sobre suas compras. Utilize as tools disponíveis. Seja educado, amigável e direto ao ponto. Chame o cliente sempre pelo nome.",
        tools=[get_client_recent_purchases, get_client_info]
    )

    while True:
        
        try:
            user_input: str = input('User: ')
            print('\n')

            if user_input == "sair":
                print("Fechando o chat...")
                session.close()
                break

            result: RunResult = Runner.run_sync(
                starting_agent=agente_de_atendimento, 
                input=user_input,
                context=client,
                session=session
            )
    
            print(f"Assistant: {result.final_output}\n")
        except KeyboardInterrupt as e:
            session.close()
            break

"""

"""
