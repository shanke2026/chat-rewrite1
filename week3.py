def calc(a, b, op="+"):
    """做四则运算，op 支持 + - * /,默认加法"""
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            return "不能除以零"
        else:
            return a / b
    else:
        return "不认识的符号"    

    





print(calc(3, 5)) 
print(calc(10, 0, "/"))   