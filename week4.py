d = float(input("输入基本尺寸"))
t = float(input("输入公差值"))
def tol_range(d, t):
    return f"{d - t/2:.2f} ~ {d + t/2:.2f}"
print(tol_range(d, t))

