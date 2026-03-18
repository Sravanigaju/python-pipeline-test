import json

with open("data.json") as f:
    data = json.load(f)
    print("Data from simulated S3:", data)