a = float(input("第一个数："))
op = input("运算符：")
b = float(input("第二个数："))


if op == "+":
    print(a+b)
elif op == "-":
    print(a-b)
elif op == "*":
    print(a*b)        
elif op == "/":
    if b == 0:
        print("不能除以零")
    else:
        print(a/b)
else:
    print("运算符无法识别")            