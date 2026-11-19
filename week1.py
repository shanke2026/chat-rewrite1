def km_to_m(km):
    return km*1000

def c_to_f(c):
    return c * 9 / 5 + 32


def intro(name, age):
    return f"我叫{name},今年{age}岁"
     

def shijian(s):
    h = s//3600
    m = (s%3600)//60
    se = (s%3600)%60
    return f"{h}小时,{m}分,{se}秒"

def fanzhuan(wenzi):
    return len(wenzi), wenzi[::-1]
    

print(km_to_m(1.5))
print(c_to_f(25))
print(intro("小明", 20))
print(shijian(3661))
print(fanzhuan("文字统计实验"))
测试分支的改动
