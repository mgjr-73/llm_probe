import os
import time

import anthropic

from dotenv import load_dotenv
from prompts import PROMPT_CATEGORIES
from logger import log_record
from analyzer import analyze_response


load_dotenv()

client = anthropic.Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

def call_anthropic(prompt):
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=200,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.content[0].text


for prompt in PROMPT_CATEGORIES["baseline"]:
    start_time = time.time()
    response = call_anthropic(prompt)
    flags = analyze_response(response)
    end_time = time.time()

    latency = round(end_time - start_time, 3)

    record = {
    "category": "baseline",
    "prompt": prompt,
    "response": response,
    "response_length": len(response),
    "latency": latency,
    "flags": flags
    }

    log_record(record)

    print("Prompt:")
    print(prompt)

    print("Response:")
    print(response)

    print(f"Response time: {latency:.2f} seconds")

    print(f"Flags: {', '.join(map(str, flags or []))}")

    print("-" * 40)