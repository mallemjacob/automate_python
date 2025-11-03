class Dog:
    def __init__(self, sound):
        self.sound = sound

    def speak(self):
        return print(f"The dog says", self.sound)
    
class Cat:
    def __init__(self, sound):
        self.sound = sound

    def speak(self):
        return print(f"The cat says", self.sound)
    
class Bird:
    def __init__(self, sound):
        self.sound = sound

    def speak(self):
        return print(f"The bird says", self.sound)
    

d1 = Dog('bark')
c1 = Cat('meow')
b1 = Bird('tweet')

animalsList = [d1, c1, b1]

for i in animalsList:
    i.speak()
