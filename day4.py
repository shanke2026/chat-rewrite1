expenses = ["苹果","橘子","葡萄"]
for shuiguo in expenses:
    print(shuiguo)


user = {"姓名":"小明","年龄":20,"城市":"山东"}
print(user["姓名"])

messages = [
    {"role": "user", "content": "你好"},
    {"role": "assistant", "content": "我不好"},
]  
for meg in messages:
    print(meg["role"])
    print(meg["content"])