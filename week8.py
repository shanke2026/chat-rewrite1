def check_size(size):
    if size <= 0:
        raise ValueError("尺寸必须大于 0")
try:
    size = float(input("尺寸"))
    check_size(size)
except ValueError as e:    
    print(e)
else:
    print("合格") 
finally:
    print("检查完毕")