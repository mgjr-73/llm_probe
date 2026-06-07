from prompts import PROMPT_CATEGORIES
from logger import log_record

def fake_llm(prompt):
    return f"You asked: {prompt}"


for prompt in PROMPT_CATEGORIES["baseline"]:
    response = fake_llm(prompt)

    record = {
    "category": "baseline",
    "prompt": prompt,
    "response": response
    }

    log_record(record)

    print("Prompt:")
    print(prompt)

    print("Response:")
    print(response)

    print("-" * 40)