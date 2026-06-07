from prompts import PROMPT_CATEGORIES


def fake_llm(prompt):
    return f"You asked: {prompt}"


for prompt in PROMPT_CATEGORIES["baseline"]:
    response = fake_llm(prompt)

    print("Prompt:")
    print(prompt)

    print("Response:")
    print(response)

    print("-" * 40)