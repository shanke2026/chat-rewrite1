
def count_even(nums):
    w = 0
    for m in nums:
        if m% 2 == 0:
            w += 1
    return w    
print(count_even([1, 2, 3, 4, 6]))



workpieces = [
    {"id": "A001", "size": 50},
    {"id": "A002", "size": 30},
    {"id": "A003", "size": 80},
    {"id": "A004", "size": 20},
]
z = 0
total = 0
for t in workpieces:
    
    if t["size"] >= 40:
        z += 1
        total += (t["size"])
        print(t["id"])
print(total / z)

def read_safe(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "文件不存在"
print(read_safe("dirty.txt")) 
print(read_safe("不存在.txt"))