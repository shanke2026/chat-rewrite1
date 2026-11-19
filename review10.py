import re
p = "A001 尺寸50 公差20"
print(re.findall(r"\d+",p ))


x = "尺寸50.5 公差0.02"
print(re.findall(r"\d+\.\d+",x))

m = "A001尺寸50±0.02"
print(re.findall(r"±(\d+\.\d+)",m))

t = "尺寸:50mm, 长度:120mm"
print(re.sub(r"mm", "", t))