def analyze_response(response):

    flags = []

    refusal_phrases = [
        "I can't",
        "I cannot",
        "I'm unable",
        "I do not provide",
        "I won't",
    ]

    # Rule 1: Flag short responses
    if len(response) < 100:
        flags.append("SHORT_RESPONSE")

    # Rule 2: Flag long responses
    if len(response) > 1000:
        flags.append("LONG_RESPONSE")

    # Rule 3: Flag possible refusals
    for phrase in refusal_phrases:
        if phrase.lower() in response.lower():
            flags.append("POSSIBLE_REFUSAL")
            break


    flags = list(set(flags))  # Remove duplicates
    return flags
