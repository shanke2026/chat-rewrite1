import random 
target = random.randint(1, 100)
count = 0   
while True:    
    n = int(input("请输入数字"))
    count += 1
    if n > target:
        print("大了")
    elif n < target:
        print("小了")
    else:
        print("对了")
        break
print(count)             