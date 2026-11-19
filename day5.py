with open ("fruits.txt", "w", encoding="utf-8") as f:
    f.write("草莓\n梨子\n葡萄\n")

with open ("fruits.txt", "r", encoding="utf-8") as f:
    print(f.read())
