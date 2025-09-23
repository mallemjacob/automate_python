# Return the sum of the numbers in the array, 
# returning 0 for an empty array. 
# Except the number 13 is very unlucky, 
# so it does not count and numbers
# that come after a 13 and it's next number.

def sum13(nums):
    count = 0
    for i in range(len(nums)):
        if nums[i] == 13 or nums[i - 1] == 13:
            # print(nums[i], nums[i - 1])
            continue
        else:
            count = count + nums[i]
    print(count)

sum13([1, 2, 3, 1, 13, 7 ,8]) #15
sum13([1, 2, 3, 2, 13, 4 ,1]) #9