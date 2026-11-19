import re
records = []
x = 0
with open("dirty.txt", "r", encoding="utf-8") as f:
    
    for line in f:
        parts = [x.strip() for x in line.split(",")]
        if len(parts) != 3: 
            x += 1
            continue
        records.append({
            "id": parts[0],
            "size": re.findall(r"\d+\.?\d*", parts[1])[0],
            "tol": re.findall(r"\d+\.?\d*", parts[2])[0],
        })
with open("clean.csv", "w", encoding="utf-8") as f:
    f.write("id,size,tol\n")
    for w in records:
        f.write(f"{w['id']},{w['size']},{w['tol']}\n")
        
print(records)
print(x)