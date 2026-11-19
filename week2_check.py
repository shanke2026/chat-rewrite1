from pathlib import Path

results = []

for p in Path("data").glob("*.txt"):
    try:
        with open(p, "r", encoding="utf-8") as f:
            text = f.read()
        lines = [l for l in text.split("\n") if l.strip()]
        results.append({"name": p.name, "count": len(lines), "status": "正常"})
    except UnicodeDecodeError:
        results.append({"name": p.name, "count": 0, "status": "读取失败"})

with open("summary.csv", "w", encoding="utf-8", newline="") as f:
    f.write("文件名,行数,状态\n")
    for r in results:
        f.write(f"{r['name']},{r['count']},{r['status']}\n")
    
    

  