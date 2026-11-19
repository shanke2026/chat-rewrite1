n = input("请输入数字")
try:
    int(n)
    print("你输入的是",n)
except ValueError:
    print("输入有误，请输入数字")
