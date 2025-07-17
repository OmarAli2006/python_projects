#Programa que integra la api de DeepSeek para generar un chat completions
# Requiere instalar la libreria openai  

from openai import OpenAI

client = OpenAI(api_key="your_api_key_here", 
                base_url = "https://openrouter.ai/api/v1")

chat = client.chat.completions.create(
    model="deepseek/deepseek-r1:free",
    messages=[
        {
            "role":"user",
            "content":"crea el codigo en python para identificar si una palbra ers palindromo"
        }
    ],
    max_tokens=1000,
    temperature=0.7,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    stop=None
)
print(chat)
