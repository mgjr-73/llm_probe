import json


def log_record(filename, record):
    """
    Save one record to a JSON file.
    """

    with open(f"results/{filename}_results.jsonl", "a") as file:
        file.write(json.dumps(record) + "\n")