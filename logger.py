import json


def log_record(record):
    """
    Save one record to a JSON file.
    """

    with open("results/results.jsonl", "a") as file:
        file.write(json.dumps(record) + "\n")