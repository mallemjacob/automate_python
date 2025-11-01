# Add an attribute called flavors that
# stores a list of ice cream flavors. 
# Write a method that displays these flavors.
# Create an instance of IceCreamStand, and call this method.

import grapef

class Restaurant:
    def __init__(self):
        pass


# gf1 = GrapeFalvours('Vitaceae','Yes')

#['black current','buttescotch','vanilla']
class IceCreamStand(Restaurant):
    def __init__(self, icecreams):
        super().__init__()
        self.flavours = icecreams
        self.grapeFamilyFlavour = grapef.GrapeFalvours('Vitaceae','Yes')
            
    def listflavours(self):
        for i in self.flavours:
            print(i)

ice1 = IceCreamStand(['black current','buttescotch','vanilla'])
ice2 = IceCreamStand(['mango','grape','orange'])

ice1.listflavours()
ice2.listflavours()
print(ice1.grapeFamilyFlavour.getGrapeFamily())
print(ice1.grapeFamilyFlavour.grape_family)
print(ice1.grapeFamilyFlavour.grape_processed)

