import re

text = "A001 尺寸50 公差20"

print(re.findall(r"\d+", text))
print(re.sub(r" +", "", text))


wenben = "尺寸50.5 公差±0.02 长度120.75"
print(re.findall(r"\d+\.\d+",wenben))

tiqv = "A001尺寸50±0.02 A002尺寸30±0.01"
print(re.findall(r"±(\d+\.\d+)",tiqv))

qingxi = "尺寸:50mm, 公差:+0.02mm, 长度:120mm"
print(re.sub(r"mm", "", qingxi))