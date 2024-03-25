import openai
from src.settings import OPEN_AI_KEY
from openai import OpenAI


client = OpenAI(api_key=OPEN_AI_KEY)
openai.api_key = 'your_openai_api_key'


def get_response_from_openai(prompt, question):
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful educator."},
        {"role": "user", "content": "Hello!"}
    ]
    )
    return completion.choices[0].message


def get_prompt():
    pass

