class Detector:                 
    def name(self):
        return "检测器"
class ParallelDetector(Detector):
    def name(self):
        return "平行度检测"
class AngleDetector(Detector):
    def name(self):
        return "角度检测"
p = ParallelDetector()
a = AngleDetector()
d = Detector()
print(d.name())
print(p.name())
print(a.name())