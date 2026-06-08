
import os
import time

import anthropic

from dotenv import load_dotenv
from prompts import PROMPT_CATEGORIES
from logger import log_record
from analyzer import analyze_response
from datetime import datetime

load_dotenv()

# Create results directory if it doesn't exist
os.makedirs("results", exist_ok=True)

# Generate file date and run ID for logging
filename = datetime.now().strftime("%Y-%m-%d")
run_id = datetime.now().strftime("%Y%m%d_%H%M%S")


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
    timestamp = datetime.now().isoformat()
    start_time = time.time()
    response = call_anthropic(prompt)
    flags = analyze_response(response)
    end_time = time.time()

    latency = round(end_time - start_time, 3)

    record = {
    "timestamp": timestamp,
    "run_id": run_id,
    "category": "baseline",
    "prompt": prompt,
    "response": response,
    "response_length": len(response),
    "latency": latency,
    "flags": flags
    }

    log_record(filename, record)

    print("Prompt:")
    print(prompt)

    print("Response:")
    print(response)

    print(f"Response time: {latency:.2f} seconds")

    print(f"Flags: {', '.join(map(str, flags or []))}")

    print("-" * 40)