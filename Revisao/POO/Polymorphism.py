class Cat:
    def sound(self):
        print('miauu')

class Dog:
    def sound(self):
        print('Auau')

class Galo:
    def sound(Self):
        print('Cocoricó')

def animal_sound(animal):
    animal.sound()

cat = Cat()
dog = Dog()
galo = Galo()

animal_sound(cat)
animal_sound(dog)
animal_sound(galo)


