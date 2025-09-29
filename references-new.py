# sequence types

# 1.list
# 2. strings

# spam = ['cat','mat','fat']
# print(spam[0])
# print(spam[1])
# print(spam[2])

# spam_str = 'valkyrie'
# print(spam_str[0])
# print(spam_str[1])
# print(spam_str[2])

# immutable and mutable types
# mutable = can change
# immutable = can't change

#list = mutable
# only references are stored in the variables, not values.
spam = ['cat','mat','fat']
cheese = spam
cheese[0] = 'hello'

print(spam)
print(cheese)

print(id(spam))
print(id(cheese))

name = 'julia'
new_name = name

print(name)
print(new_name)
print(id(name))
print(id(new_name))
name = 'valkyrie'
print(name)

print(id(name))
print(id(new_name))

def greet(list_name):  #575736363
    list_name.append('hello')

spam = ['cat','mat','tat'] #575736363
print(spam)

greet(spam)  #575736363

print(spam)