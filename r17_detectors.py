class Detector:
    def name(self):
        return "检测器"
    def check(self,value, limit):
        return value <= limit

class RoughnessDetector(Detector):
    def name(self):
        return "粗糙度检测"
class HardnessDetector(Detector):
    def name(self):
        return "硬度检测"
    def check(self,value, limit):
        return value >= limit