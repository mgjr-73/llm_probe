import json

records = []
latencies = []
refusals = 0
total_length = 0

# Load records from the JSONL file
with open("results/results.jsonl", "r") as file:
    for line in file:
        records.append(json.loads(line))

for record in records:
    # Count refusals
    if "POSSIBLE_REFUSAL" in record.get("flags", []):
        refusals += 1

    # Calculate average response length
    total_length += record.get("response_length", 0)
    average_length = total_length / len(records)

    # Calculate average latency
    if "latency" in record:
        latencies.append(record["latency"])
    average_latency = sum(latencies) / len(latencies) if latencies else 0


print(f"Total records: {len(records)}")       
print(f"Refusals: {refusals}")
print(f"Average response length: {average_length:.2f}")
print(f"Average latency: {average_latency:.2f} seconds")