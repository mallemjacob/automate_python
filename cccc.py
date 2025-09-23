#local scope and global scope

#local scope is created when function is called.
# def spam():
#     name = 'julia'
#     print(name)

# spam()
# print(name)

# global scope is outside of all functions.
# global scope is created when program runs.

# distance = 99 #glbal scope #10


# def ham():
#     distance = 10 #global scope
#     print(distance)
    
# ham()
# print(ham())


# print(len('hello'))
# print(print('hello'))


# variables from one local scope cant be accessed from another local scope.

name = 'valkyrie'

def spam():
    name = 'julia'
    ham()
    print(name) # local variable

def ham():
    print(name) # global variable

spam() # calling a fucntion   