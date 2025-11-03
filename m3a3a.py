# Módulo 3, Aula 3
from typing import List
from agents import Agent, Runner, RunResult, SQLiteSession

from helper import get_agent, get_session
from tools import get_client_recent_purchases, get_client_info, dynamic_client_instructions

from models import Cliente, Compra, Produto

def main() -> None:
    agent: Agent = get_agent(
        name="Agente de Suporte Dinâmico",
        instructions=dynamic_client_instructions,
        tools=[get_client_info, get_client_recent_purchases]
    )

    session: SQLiteSession = get_session('chat_3')

    compras: List[Compra] = [
        Compra(id='001', produto=Produto(nome='Playstation 5', preco=499.57)),
        Compra(id='002', produto=Produto(nome='Mortal Kombat 1', preco=19.21)),
        Compra(id='003', produto=Produto(nome='TV LG 65', preco=1219.34)),
        Compra(id='004', produto=Produto(nome='Lavadora Samsung', preco=434.89)),
        Compra(id='005', produto=Produto(nome='Geladeira Arno', preco=2319.45))
    ]
    cliente1_info: Cliente = Cliente(id='001', nome='Ray Sychev', compras=compras)

    while True:
        try:
            user_input = input("User: ")
            print('\n')

            if user_input == 'sair':
                print("Chat finalizado...")
                break
        
            result: RunResult = Runner.run_sync(starting_agent=agent, input=user_input, context=cliente1_info, session=session)
            print(f"Assistant: {result.final_output}\n")
        except KeyboardInterrupt as e:
            break


if __name__ == '__main__':
    main()
