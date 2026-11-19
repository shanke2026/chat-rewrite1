import json
workpieces = [
    {"id": "A001", "size": 50, "tol": 0.02},
    {"id": "A002", "size": 30, "tol": 0.01},
    {"id": "A003", "size": 80, "tol": 0.03},
]

with open("workpieces.json", "w", encoding="utf-8") as f:
    json.dump(workpieces, f, ensure_ascii=False, indent=2)

with open("workpieces.json", "r", encoding="utf-8") as f:
    data = json.load(f)
print(data[0]["id"])
print(data[0]["size"])