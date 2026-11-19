class Detector:
    def name(self):
        return "检测器"
class ParallelDetector(Detector):
    def name(self):
        return "平行度检测"
class AngleDetector(Detector):
    def name(self):
        return "角度检测"
a = Detector()
b = ParallelDetector()
c = AngleDetector()
print(a.name())
print(b.name())
print(c.name())