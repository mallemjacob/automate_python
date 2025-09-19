# print('hi')
# print(1+2)


# def cat_dog(str):
#   """
#   Checks if the number of 'cat' and 'dog' substrings are equal in a given string.

#   Args:
#     str: The input string.

#   Returns:
#     True if the counts are equal, False otherwise.
#   """
#   cat_count = 0
#   dog_count = 0
#   for i in range(len(str)):
#     if str[i:i+3] == 'cat':
#       cat_count += 1
#     if str[i:i+3] == 'dog':
#       dog_count += 1
#   return cat_count == dog_count

# print(cat_dog('catdog'))
# print(cat_dog('catcat'))
# print(cat_dog('1cat1cadodog'))
# print(cat_dog('catcatdogdog'))

# def demo(s1='s1111',s2='s2222'):
#     print(s1 + ' ' + s2)


# demo(s2='hi', s1='there')
# demo()


#*************************************************



def cat_dog(str):
    
    cat_count = 0
    dog_count = 0

    for i in range(len(str)):
        if str[i:i+3] == 'cat':
            cat_count = cat_count + 1
        if str[i:i+3] == 'dog':
            dog_count = dog_count + 1
    return cat_count == dog_count 


print(cat_dog('catdog'))
print(cat_dog('catcat'))
print(cat_dog('1cat1cadodog'))
print(cat_dog('catcatdogdog'))