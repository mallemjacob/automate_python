# After looping through the list and printing "name" key
# create a seperate file for callApi method
# Then import that class modules into this github_class.py file
# as instance attibute.
# Create a new list and append the values into the list.
# use list concatnation or append method
# Write new metod to print the names from the list.

import requests

class Github:
    def __init__(self, path):
        self.path = path
        self.names = []

    def callApi(self):
        response = requests.get(self.path)
        # convert json data to python dictionary
        data = response.json()
        # print(data["items"][0]["id"])

        for item in data["items"][:5]:
            self.names = self.names + [item["name"]]

        # print(self.names)

    def getNamesList(self):
        for i in self.names:
            print(i)

ghlink = "https://api.github.com/search/repositories?q=language:python+sort:stars"
req1 = Github(ghlink)
req1.callApi()
req1.getNamesList()
