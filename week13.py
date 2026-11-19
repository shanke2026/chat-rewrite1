class Workpiece:
    def __init__(self, id, size):
        self.id = id
        self.size = size

    def is_big(self):
        return self.size >= 40
    def describe(self):
        return f"{self.id}尺寸{self.size}"

a = Workpiece("A001", 50)
b = Workpiece("A002", 30)
print(a.id)        
print(a.size)      
print(a.is_big())  
print(b.id)        
print(b.size)      
print(b.is_big())
print(a.describe())
print(b.describe())