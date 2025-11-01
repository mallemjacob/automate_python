#Import code from restaurants file

import restaurants

class Asian():
    def __init__(self):
        self.stars = restaurants.Restaurant() #5

    def getStars(self):
        return f"This is a {self.stars.st} start restaurant."
    
asian_res_1 = Asian()
print(asian_res_1.getStars())
print(asian_res_1.stars.st)