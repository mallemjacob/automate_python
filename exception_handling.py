# try:
#     code
# except TypeError:
#     handling code

# TypeError
# def spam(name):
#     try:    
#         print('Hi ' + name)
#     except TypeError:
#         print('Must be integer')
        

# spam('bill')
# spam(4)
# spam('jjj')
# spam('')

# def spam(name):
# if    
#     return ''

# def ind(mylist):
#     try:
#         user_ind_input = int(input('Enter an index: '))
#         print(mylist[user_ind_input])
#     except IndexError:
#         print('Error: index error')

# ind(['car','keys'])

# try:
#     code block
# except Error:
#     code block
# except Error:
#     code block

def con_str(name):
    print('Hi ' + name)


arg = input('Enter a name: ')
if arg.isdecimal():
    print('Must be alphabet')
try:
    con_str(arg)
except TypeError:
    con_str(str(arg))
