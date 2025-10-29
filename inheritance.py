#inheritance = passing down certain attributes to the offspring

#parents ----> #child


# parent class
class Animal:
    def __init__(self, species):
        self.species = species

    def describe_species(self):
        return f"This belongs to {self.species} species."
    
# dog child class
class Dog(Animal):
    def __init__(self, species, name):
        super().__init__(species)
        self.name = name

    def getname(self):
        return f"Name is {self.name}"

dog1 = Dog('german shepard', 'snoopy')
print(dog1.species)

print(dog1.describe_species())
print(dog1.getname())


# cat child class
class Cat(Animal):
    def __init__(self, species, age):
        super().__init__(species)
        self.age = age

    def getCatAge(self):
        return f"The age is {self.age}"

cat1 = Cat('zookie', 18)
print(cat1.species)
print(cat1.describe_species())
print(cat1.getCatAge())

# def fun2(arg2):
#     print(f'This is from arg2: {arg2}')

# def fun1(arg1):
#     fun2(arg1)

# fun1('Hello')


# spam = []
# spam.index()
# spam.appned()

# name = 'hi'
# name.capitalize()
# name.lower()