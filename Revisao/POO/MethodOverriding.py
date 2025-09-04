class Parente():
    def show(self):
        print('Parente method')

class Children(Parente):
    def show(self):
        print('Child method')


obj = Children()
obj.show()
