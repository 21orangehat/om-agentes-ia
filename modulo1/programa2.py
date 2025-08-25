from agents import Agent, Runner, RunResult

from core.helpers import get_agent, get_weather

def main() -> None:
    agente: Agente = get_agent(
        name="Agente de Previsão do Tempo",
        instructions="Você é um agente de previsão do tempo. Responda sempre em português do Brasil e de forma muito formal.",
        tools=[get_weather,]
    )

    result: RunResult = Runner.run_sync(
        starting_agent=agente, 
        input="Como está o clima em Braga?"
    )

    print(result.final_output)


"""
Para criar agentes, fazemos uso de 4 argumentos principais:
- name: O nome do agente, usado para identificar cada agente. 
Geralmente nomeamos o agente de forma que sua função seja
entendida de forma explícita.
- instructions: Instruções passadas para o agente de forma que
possamos passar: Tom de voz, personalidade, metas a serem atingidas,
caminhos para serem seguidos, limites*, etc;
O argumento 'instructions' é conhecido também como system_prompt
pois se refere justamente ao prompt passado às LLM.
* Para limites de segurança, fazemos uso de Guardrails...
- model: O modelo de IA a ser usado no agente...
- tools (opcional): Para agentes de IA este é considerado
o mais importante argumento, pois é o que transforma uma IA
que gera apenas texto para uma que pode fazer qualquer coisa.
"""
"""
Prezado(a) senhor(a),

Informo que o clima na cidade de Braga apresenta-se nublado.

Atenciosamente,

Seu agente de previsão do tempo.
"""
