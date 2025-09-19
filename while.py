# i = 1
# while True:
#     print(i)
#     if i == 5:
#         break
#     i = i + 1


# spam = 0
# while spam < 5:
#     print('Hello world!')
#     spam = spam + 1

# catNames = []

# while True:
#   cat_name_input = input('Enter the cat name here, kiddo: ')
#   if cat_name_input == '':
#     break
#   elif cat_name_input in catNames:
#     print('The cat already exists. Try a different name!')
#   else:  
#     catNames =  catNames + [cat_name_input]

# for i in catNames:
#   print(i)


# supplies = ['pens', 'staplers', 'flamethrowers', 'binders']

# for i in range(len(supplies)):
#   print('Index ' + str(i) + ' in supplies is: ' + supplies[i])


# supplies = ['pens', 'staplers', 'flamethrowers', 'binders']

# for index, item in enumerate(supplies):
#   print('Item ' + item + ' is at index ' + str(index))


# import random

# print(random.choice(supplies))
# random.shuffle(supplies)
# print(supplies)

# print(supplies[random.randint(0, len(supplies) - 1)])

def xyz_there(str):
  if str[:3] == "xyz":
    return True
                    
  for i in range(1, len(str) - 2):
    if str[i-1] != "." and str[i:i+3] == "xyz":
      return True
                                      
  return False

print(xyz_there('abcxyz'))  #z=5, 6
print(xyz_there('abc.xyz')) #3=. 4=x
print(xyz_there('.xyz.abc'))


spam = ['a', 'b', '.', 'x', 'y', 'z']

for i in range(len(spam) -2):  #i=a = 0
  if spam[i:i+3] == ['x','y','z']:
    print(True)