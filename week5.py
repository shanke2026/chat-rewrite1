workpieces = [
    {"id": "A001", "size": 50, "tol": 0.02},
    {"id": "A002", "size": 30, "tol": 0.01},
    {"id": "A003", "size": 80, "tol": 0.03}
]
for i in workpieces:
    print(i["id"], i["size"])
workpieces.append({"id": "A004", "size": 100, "tol": 0.05})
del workpieces[0]
target = input("输入要查的 id：")
for w in workpieces:
    if w["id"] == target:
        print(w)
        break
else:
    print("没找到")
