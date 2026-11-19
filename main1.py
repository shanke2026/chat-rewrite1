import detectors
p = detectors.ParallelDetector()
a = detectors.AngleDetector()
pass_count = 0
results = []
with open("sharp_data.txt", "r", encoding="utf-8")as f:
    for line in f:
        parts = line.strip().split(",")
        ok_parallel = p.check(float(parts[1]), float(parts[3]))
        ok_angle = a.check(float(parts[2]), float(parts[4]))
        if ok_parallel and ok_angle:
            results.append({"工件":parts[0], "结果":"合格"})
            pass_count += 1
            print(parts[0], "合格")
        else:
            results.append({"工件":parts[0], "结果":"超差"})
            print(parts[0], "超差")

with open("report.txt", "w", encoding="utf-8")as f:
    f.write("工件,结果\n")
    for r in results:
        f.write(f"{r['工件']}, {r['结果']}\n")
print(pass_count/len(results)*100)    


