class Detector:
    def name(self):
        return "检测器"

    def check(self, value, limit):
        return value <= limit
class ParallelDetector(Detector):
    def name(self):
        return "平行度检测"
class AngleDetector(Detector):
    def name(self):
        return "角度检测"
p = ParallelDetector()
print(p.name(), p.check(0.02, 0.05))