
import csv
row = []


with open("workpieces.csv", "r", encoding="utf-8", newline="") as f:
    for m in csv.reader(f):
        row.append(m)
data = row[1:]
big = [r for r in data if float(r[1]) >= 40]            
with open("big.csv", "w", encoding="utf-8", newline="") as f:
    for w in row:
        f.write(f"{w[0]},{w[1]},{w[2]}\n")
print(len(big))
        


