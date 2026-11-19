import json
x = [
    {"id": "A001", "size": 50, "tol": 0.02},
    {"id": "A002", "size": 30, "tol": 0.01},
    {"id": "A003", "size": 80, "tol": 0.03},
]
with open("review.json","w", encoding="utf-8") as f:
    json.dump(x,f)
with open("review.json","r", encoding="utf-8") as f:
    m = json.load(f)
print(m[0]["id"],m[0]["size"])