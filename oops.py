class Dog:
    """A simple attempt to model a dog."""
    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age
    
    def sit(self):
        """Simulate a dog sitting in respond to a command."""
        print(f"{self.name} is now sitting.")
    
    def roll(self):
        """Simulate rolling over in respond to a command."""
        print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6)
your_dog = Dog('Zophie', 8)

dogs = [my_dog, your_dog]

for dog in dogs:
    print(f"My dog's name is {dog.name}.")
    print(f"My dog is {dog.age} years old.")


