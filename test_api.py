import os
import anthropic

from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=100,
    messages=[
        {
            "role": "user",
            "content": "What is Python?"
        }
    ]
)

print(response.content[0].text)