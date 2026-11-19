workpieces = [
    {"id": "A001", "size": 50, "tol": 0.02},
    {"id": "A002", "size": 30, "tol": 0.01},
    {"id": "A003", "size": 80, "tol": 0.03},
]

with open("workpieces.csv", "w", encoding="utf-8", newline="") as f:
    f.write("id,size,tol\n")
    for w in workpieces:
        f.write(f"{w['id']},{w['size']},{w['tol']}\n")
import csv

with open("workpieces.csv", "r", encoding="utf-8", newline="") as f:
    for row in csv.reader(f):
        print(row)