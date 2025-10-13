# try:
#     code
# except TypeError:
#     handling code

# TypeError
# def spam(name):
#     try:
#         print('Hi ' + name)
#     except TypeError:
#         print('Error: Invalid Input')

# spam('hhh')
# spam(4)
# spam('jjj')
# spam('')

# def spam(name):
# if    
#     return ''

def ind(mylist):
    try:
        user_ind_input = int(input('Enter an index: '))
        print(mylist[user_ind_input])
    except IndexError:
        print('Error: index error')

ind(['car','keys'])