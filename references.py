def greet(mylist):
    if isinstance(mylist, str):
        print(mylist)
    else:
        mylist.append('brown')



name = 'valkyrie'
colors = ['red','green','blue']
print(colors)
greet(name)
greet(colors)
print(colors)

def eggs(someParameter):
    someParameter.append('Hello')
    print(id(someParameter))
spam = [1, 2, 3]
eggs(spam)
print(spam)

print(id(spam))