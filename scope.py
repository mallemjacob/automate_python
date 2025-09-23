# local and globle scope

# Local Variables Cannot Be Used in the Global Scope
# def spam():
#     eggs = 1337
# spam()

# print(eggs)

# Local Scopes Cannot Use Variables in Other Local Scopes
# def spam():
#     eggs = 99
#     bacon()
#     print(eggs)

# def bacon():
#     ham = 101
#     eggs = 0

# spam()    

# Global Variables Can Be Read from a Local Scope
# def spam():
#     print(eggs)
# eggs = 42
# spam()
# print(eggs)

# Local and Global Variables with the Same Name    
# def spam():
#     eggs = 'spam local'
#     print(eggs)

# def bacon():
#     eggs = 'bacon local'
#     print(eggs)
#     spam()
#     print(eggs)

# eggs = 'global'
# bacon()
# print(eggs)

#global statement
# def spam():
#     global eggs
#     eggs = 'spam'

# eggs = 'global'
# spam()
# print(eggs)

#######################################
# def spam():
#     global eggs
#     eggs = 'spam'

# def bacon():
#     eggs = 'bacon'   #local variable = 'bacon'
#     print(eggs)

# def ham():
#     print(eggs)  # spam

# eggs = 42   #spam
# spam()
# bacon()
# ham()
# print(eggs)  #spam    