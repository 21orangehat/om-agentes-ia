from uuid import uuid4

from agents import (
    Agent, 
    Runner, 
    RunResult,
    RunContextWrapper
)

from core.helpers import (
    get_agent,
    get_session,
    get_weather,
    get_client_recent_purchases,
    get_client_info,
    dynamic_client_instructions
)

from core.models import Cliente, Compra


def main() -> None:
    client1: Cliente = Cliente(
        id=uuid4().__str__(),
        nome='Ray Sychev',
        compras=[
            Compra(id=uuid4().__str__(), produto="PlayStation 5", preco=499.99),
            Compra(id=uuid4().__str__(), produto="Silent Hill 2", preco=67.34),
            Compra(id=uuid4().__str__(), produto="Candy", preco=9.00),
            Compra(id=uuid4().__str__(), produto="Pendrive 32GB", preco=29.26),
        ]
    )

    client2: Cliente = Cliente(
        id=uuid4().__str__(),
        nome='Diemesleno Carvalho',
        novo=False,
        compras=[
            Compra(id=uuid4().__str__(), produto="PlayStation 5", preco=399.99)
        ]
    )

    session: SQLiteSession = get_session(session_id="m3chat_3") 

    agente_de_suporte: Agent = get_agent(
        name="Agente de Suporte Dinâmico",
        instructions=dynamic_client_instructions,
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
                starting_agent=agente_de_suporte, 
                input=user_input,
                context=client2,
                session=session
            )
    
            print(f"Assistant: {result.final_output}\n")
        except KeyboardInterrupt as e:
            session.close()
            break

"""
User: Olá, tudo bem?


Assistant: Olá, Ray Sychev! Tudo bem por aqui, e com você? Seja muito bem-vindo à plataforma! 😊

Estou aqui para te ajudar a se familiarizar com tudo e responder a qualquer dúvida que você tiver. Como você é novo por aqui, que tal começarmos com o básico?

Primeiro, temos duas funções principais que podem ser muito úteis para você:

*   **`get_client_info()`**: Essa função é como se fosse um "cartão de identificação" seu aqui na plataforma. Ela te mostra as suas informações de cliente, como nome, e-mail e outras coisas importantes.

*   **`get_client_recent_purchases(n: int)`**: Essa função é ótima para você acompanhar suas últimas compras. Basta dizer quantas compras você quer ver (por exemplo, as últimas 3) e ela te mostra tudo direitinho.

Se você quiser, podemos começar explorando essas funções. Que tal começarmos vendo as suas informações de cliente? É só me avisar! 😉

-----------
User: Como funciona a plataforma?


Assistant: Ótima pergunta, Ray! Para entender como a plataforma funciona, imagine que ela é como uma loja online personalizada, onde você tem acesso a informações importantes sobre a sua conta e suas compras.

**Essencialmente, a plataforma funciona da seguinte forma:**

1.  **Você (o cliente):** Você é o centro de tudo! A plataforma existe para te ajudar a ter a melhor experiência possível.
2.  **As Funções:** As funções (`get_client_info()` e `get_client_recent_purchases(n: int)`) são como "ferramentas" que te dão acesso a diferentes informações e funcionalidades.
3.  **A Interface (eu!):** Eu sou a interface entre você e as funções. Você me diz o que você quer fazer (por exemplo, "Quero ver minhas informações") e eu uso as funções para buscar as informações e te mostrar de forma clara e organizada.

**Explicando as funções em mais detalhes:**

*   **`get_client_info()`:** Quando você usa essa função, a plataforma busca no banco de dados todas as informações associadas à sua conta (Ray Sychev). Isso pode incluir seu nome, endereço de e-mail, data de cadastro, etc. A função então me entrega essas informações, e eu as mostro para você.
*   **`get_client_recent_purchases(n: int)`:** Essa função é um pouco mais "específica". Quando você a usa, você precisa dizer para ela quantas compras recentes você quer ver (esse é o "n"). Por exemplo, se você digitar `get_client_recent_purchases(n=5)`, a plataforma vai buscar as suas 5 compras mais recentes, me entregar a lista, e eu vou mostrar para você.

**Em resumo:** Você me diz o que quer saber, eu uso as funções para buscar as informações no sistema, e te mostro tudo de forma organizada.

Compreendeu como funciona? Se tiver alguma dúvida, pode perguntar! 😊
"""
