class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} is located in UK.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is a {self.cuisine_type} restaurant.")


def call_restaurant(restaurant):
    print(f"The restaurant is {restaurant.restaurant_name}")
    print(f"It is a {restaurant.cuisine_type} restaurant")

    restaurant.describe_restaurant()
    restaurant.open_restaurant()

restaurants_list = []

while True:
    resurant_name = input("Enter resurant name: ")
    if resurant_name == '':
        break
    cusine_type = input('Enter cusine type: ')
    if resurant_name and cusine_type == '':
        break
    restaurant = Restaurant(resurant_name, cusine_type)
    restaurants_list = restaurants_list + [restaurant]
    call_restaurant(restaurant)

print('The restaurants are:')
for i in restaurants_list:
    print(i.restaurant_name + ' --- ' + i.cuisine_type)