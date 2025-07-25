import openai
from core.config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def get_chat_response(prompt: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "당신은 시민 권리 상담 전문가입니다."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content
