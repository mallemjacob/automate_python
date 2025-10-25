import requests

URL = "https://fakerestaurantapi.runasp.net/api/Restaurant"

response = requests.get(URL)

output = response.json()

# recipes_list = output["recipes"]

# print(output["recipes"][5]["name"])

# for i in range(len(recipes_list)):
#     print(recipes_list[i]["name"])
#     print(recipes_list[i]["cuisine"])

##############################################################


for i in range(len(output)):
    print(f"{output[i]["restaurantName"]} ---- {output[i]["type"]}")