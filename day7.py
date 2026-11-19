try:
    with open ("notes.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
        pass
while True:
    user = input("请输入文字")  
    if user == "quit":
        break
    with open ("notes.txt", "a", encoding="utf-8") as f:
        f.write(user+"\n")
