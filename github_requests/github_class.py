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
        data = response.json()
        print(data["items"][0]["id"])

glink = "https://api.github.com/search/repositories?q=language:python+sort:stars"
req1 = Github(glink)
req1.callApi()