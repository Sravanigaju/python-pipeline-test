import json

data = {
    "name": "Sravani",
    "status": "processed"
}

with open("output.json", "w") as f:
    json.dump(data, f)

print("File generated successfully")
