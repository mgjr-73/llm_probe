import json


filename = "2026-06-08"

records = []
latencies = []
refusals = 0
total_length = 0

# Load records from the JSONL file
with open(f"results/{filename}_results.jsonl", "r") as file:
    for line in file:
        line = line.strip()
        if line:
            records.append(json.loads(line))

# Global analysis of records
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
print(f"==" * 20)

# Analysis by category
categories = {}

for record in records:
    category = record.get("category", "Unknown")
    if category not in categories:
        categories[category] = []

    categories[category].append(record)

for category, category_records in categories.items():
    print(f"Category: {category}")
    print(f"  Total records: {len(category_records)}")
    print(f"==" * 20)
