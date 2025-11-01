import requests

response = requests.get('https://jsonplaceholder.typicode.com/todos/1')

print(response.json())

data = response.json()

print(data['userId'])


# from google import genai

# client = genai.Client(api_key="")

# response = client.models.generate_content(
#     model="gemini-2.5-flash", contents="Can AI give response to any kind of question?"
# )
# print(response.text)