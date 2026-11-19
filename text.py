import csv
with open("workpieces.csv", "r", encoding="utf-8", newline="") as f:
    rows = list(csv.reader(f))
total = 0
for row in rows[1:]:
    total += float(row[1])
print(len(rows[1:])) 
print(total / len(rows[1:]))

              
