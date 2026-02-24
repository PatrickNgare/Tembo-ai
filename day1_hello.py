import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()               # loads your .env file

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-4o-mini",  # cheapest, best model for learning
    messages=[
        {"role": "user", "content": "What is the Masai Mara?"}
    ],
    temperature=0.7
)

print(response.choices[0].message.content)
