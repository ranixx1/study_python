class Math:
    @classmethod
    def add(cls,x,y):
        return x+y
    
    @staticmethod
    def subtract(x,y):
        return x-y
    
print(Math.add(5,4))
print(Math.subtract(120,38))