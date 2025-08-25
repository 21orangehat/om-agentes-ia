# https://openai.github.io/openai-agents-python/ref/run/
# https://medium.com/@danushidk507/openai-agents-sdk-with-ollama-fc85da11755d
# https://dev.to/itshayder/breaking-free-ai-api-keys-2025-3-secret-platforms-replacing-paid-services-2708
# https://aistudio.google.com/apikey
from agents import Agent, Runner, RunResult

from core.helpers import get_agent

def main() -> None:
    agente: Agente = get_agent(
        name="Agente Principal",
        instructions="Você é um assistente prestativo. Seja direto ao ponto."
    )

    result: RunResult = Runner.run_sync(
        starting_agent=agente, 
        input="Me escreva um poema sobre python"
    )

    print(result.final_output)

"""
Com certeza! Aqui está um poema sobre Python:

Na terra da computação, onde os códigos se encontram,
Python reina supremo, uma linguagem que encanta.
Com sintaxe clara e um estilo elegante,
É um deleite para programadores, jovens e veteranos.

Desde scripts simples até projetos complexos,
Python se adapta com facilidade e destreza.
Suas bibliotecas vastas, um tesouro a ser explorado,
Oferecem soluções para cada necessidade, sem ser ignorado.

Na ciência de dados, Python brilha intensamente,
Analisando números, revelando o que está latente.
Com Pandas e NumPy, a manipulação se torna arte,
Transformando dados brutos em insights, com destreza e faro.

No aprendizado de máquina, Python é o guia,
Construindo modelos, com precisão e magia.
TensorFlow e PyTorch, ferramentas poderosas,
Permitem que as máquinas aprendam, de formas maravilhosas.

Na web, Python se destaca com desenvoltura,
Criando sites e aplicativos, com arquitetura segura.
Django e Flask, frameworks renomados,
Agilizam o desenvolvimento, com recursos bem elaborados.

Python é mais que uma linguagem, é uma comunidade,
Unida por um espírito colaborativo, com afinidade.
Compartilhando conhecimento, aprendendo em conjunto,
Construindo um futuro digital, com foco e adjunto.

Então, se você busca uma linguagem versátil,
Que te impulsione a criar, de forma ágil e gentil,
Python é a escolha certa, não hesite em abraçar,
E descubra um mundo de possibilidades, sem se cansar.
"""
