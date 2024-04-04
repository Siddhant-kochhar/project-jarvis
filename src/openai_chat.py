import json
from src.settings import OPEN_AI_KEY
from openai import OpenAI


client = OpenAI(api_key=OPEN_AI_KEY)
prompt_file_path = "src/prompts.json"


def get_response_from_openai(prompt, question):
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": prompt},
        {"role": "user", "content": question}
    ]
    )
    return completion.choices[0].message


def get_prompt(subject, class_, proficiency):
    with open(prompt_file_path, 'r') as file:
        json_data = json.load(file)
    
    return json_data.get(subject, {}).get(class_, {}).get(proficiency, "You are a high school teacher. Be polite and help the student with their query.")

