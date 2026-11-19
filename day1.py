n = int(input("请输入数字"))
if n % 2 == 0:
    print("偶数")
else:
    print("奇数")

fenshu = int(input("请输入数字"))
expenses=["A","B","C","D"]
if fenshu >= 90:  
    print(expenses[0])
elif fenshu >= 80:
    print(expenses[1])
elif fenshu >= 60:
    print(expenses[2])
else:
    print(expenses[3])