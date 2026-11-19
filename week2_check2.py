from pathlib import Path
results = []
x = 0
for n in Path("data2").rglob("*.txt"):
    try:
        with open(n, "r", encoding="utf-8") as f:
            text = f.read()
            lines = [l for l in text.split("\n") if l.strip()]
            results.append({"name":n.name, "lines":lines})
    except UnicodeDecodeError:
        x += 1
        pass
t = 0
with open("merged.txt", "w", encoding="utf-8") as f:
    f.write("文件名: 内容\n")
    for w in results:
        for line in w["lines"]:
            f.write(f"{w['name']}:{line}\n")
            t += 1
        
print(t)
print(x)
