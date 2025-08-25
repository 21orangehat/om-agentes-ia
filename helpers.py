import os
from agents import OpenAIChatCompletionsModel, AsyncOpenAI
from dotenv import load_dotenv

load_dotenv()


def get_model():
    """"""
    model: OpenAIChatCompletionsModel = OpenAIChatCompletionsModel(
        model='gemini-2.0-flash',
        openai_client=AsyncOpenAI(
            api_key=os.environ.get('GOOGLE_AI_KEY'), 
            base_url="https://generativelanguage.googleapis.com/v1beta",
        )
    )

    return model
