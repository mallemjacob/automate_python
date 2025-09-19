# def hello():
#     print('Hello!')
#     print('Bonjour!')

# hello()
# hello()



# def call_me():
#     name = ''
#     message = "calling...."
#     while name != 'exit':
#         print('who do you wanna call?')
#         name = input()
#         if name == 'exit':
#             print('exiting....')
#             break
#         else:
#             print(message + name)
    
# call_me()


# def inner():
#     name = 'pink'
#     print(name)

# name = 'yellow'
# inner()

# print(name)

#####################################


# def sum67(nums):
#     total = 0
#     i = 0

#     while i < len(nums):
#         if nums[i] == 6:
#             for j in range(i, len(nums)):
#                 if nums[j] == 7:
#                     i = j + 1
#                     break

#         else:
#             total = total + nums[i]
#             i = i + 1
#     return total

# print(sum67([1,2,2,6,99,99,7,2]))


# spam = [1,2,2,6,99,99,7,2]
# total = 0
# ind = 0
# for i in range(ind, len(spam)):
#     if spam[i] == 6:
#         for j in range(i, len(spam)):  # 3, 8
#             if spam[j] == 7:
#                 ind = j + 1
#                 break
#     else:
#         total = total + spam[i]
        

# print(total)

#/////////////////////////////////////////

# def myfun(num1=5, num2=10):
#     return f"The numbers are num1: {num1} and num2: {num2}"

# print(myfun(num2=2,num1=3))



# def spam():
#     global eggs
#     eggs = 'spam'


# eggs = 'global'
# spam()

# print(eggs)



# def hello(name, age):
#     print('hello ' + str(name))
#     print('you are ' + str(age) + ' years old.')
#     # return 'hhhh'

# print(hello(age=28, name='valkyrie'))

# print('hello', end='')
# print('world')

# print('jan','feb','march', sep='|')

# #exception handling
# def spam(divideBy):
#     try:
#         return 42 / divideBy

#     except ZeroDivisionError:
#         print('Error: Invalid argument')
# print(spam(2))
# print(spam(12))
# print(spam(0))
# print(spam(1))


# def greet(age):
#     try:
#         return 'You are ' + age + ' years old.'
#     except TypeError:
#         print('Error: can not concantinate int and string.')

# print(greet(28))