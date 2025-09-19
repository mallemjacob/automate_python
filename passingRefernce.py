def eggs(someParameter):
    someParameter.append('Hello')

spam = [1,2,3]
print(id(spam))
print(spam)
eggs(spam)
print(id(spam))
print(spam)