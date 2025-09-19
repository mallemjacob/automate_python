# spam = ['apples','bananas','tofu','cars']
# new_spam = [1,2,3,4,5,6,7,8,9]


# def addAndFunc(list):
#     new_str = ''

#     for i in list:
#         if list.index(i) == len(list) - 1:    #  0 == 3
#             new_str = new_str + 'and ' + str(i)
#         elif list.index(i) == len(list) - 2:
#             new_str = new_str + str(i) + ' '
#         else:
#             new_str = new_str + str(i) + ', '

#     print(new_str)


# print('hi there')
# addAndFunc(spam)

# for i in [5,10,15,20,25]:
# 	if i == 20:
# 		break
# 	print(i)
	
# print('the end')

# num = 1

# while num <= 10 :
# 	print(str(num) + ':' + ' hi')
# 	num = num + 1
	
# print('the end of while loop')
	


#################################
# def sum67(nums):
#   total = 0               # total = 5
#   i = 0                  # i = 3, i = 7
  
#   while i < len(nums):   #0 < 7 # 
#     if nums[i] == 6:
#       for j in range(i,len(nums)): # 3, 7
#         if nums[j] == 7:
#           i = j + 1   # 6 + 1
#           break
#     else:
#       total += nums[i]  # 0 + 1 + 2 + 2
#       i = i + 1
#   return total

# print(sum67([1,2,2,6,99,99,7,2]))

##################################

# for i in range(3, 6):
#   print(i)


def sum67(nums):
    total = 0
    i = 0

    while i < len(nums):
        if nums[i] == 6:
            for j in range(i, len(nums)):
                if nums[j] == 7:
                    i = j + 1
                    break

        else:
            total = total + nums[i]
            i = i + 1
    return total