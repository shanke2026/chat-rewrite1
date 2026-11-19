import json

data = [
    {"id": "A001", "size": 50},
    {"id": "A002"},          
]

with open("test.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

with open("test.json", "r", encoding="utf-8") as f:
    records = json.load(f)
for item in records:
    print(item.get("id"), item.get("size","未知"))