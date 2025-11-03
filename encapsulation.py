class Animal:
    def __init__(self, species):
        self.name = 'snoopy'
        self.__species = species

    # getter
    def get_species(self):
        return f"This belongs to {self.__species} species."
    
    # setter
    def set_species(self, species):
        self.__species = species


a1 = Animal('dog')
print(a1.get_species()) #dog

# a1.__species = 'cat'

print(a1.name)
print(a1.__species)

# a1.set_species('cat')

print(a1.get_species())