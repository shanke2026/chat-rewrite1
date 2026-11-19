import r17_detectors
r = r17_detectors.RoughnessDetector()
h = r17_detectors.HardnessDetector()
results = []
pass_count = 0
with open("rough_data.txt","r",encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split(",") 
        ok_rough = r.check(float(parts[1]),float(parts[3]))
        ok_hard = h.check(float(parts[2]),float(parts[4]))
        if ok_rough and ok_hard:
            results.append({"工件":parts[0],"结果":"合格"})
            pass_count += 1
        else:
            results.append({"工件":parts[0],"结果":"超差"})
with open("report3.txt","w",encoding="utf-8") as f:
    f.write("工件,结果\n")
    for a in results:
        f.write(f"{a['工件']},{a['结果']}\n")
print(pass_count/len(results)*100)
