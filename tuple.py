# eggs = ('hello', 42, 0.5)

# print(eggs)

# print(eggs[0])
# print(eggs[1])
# print(eggs[2])

# for i in eggs:
#     print(i)


# practice

def find_xyz(str):
    if str[:3] == 'xyz':
        return True
    
    for i in range(1, len(str) - 2):
        if str[i - 1] != '.' and str[i: i + 3] == 'xyz':
            return True
    return False

print(find_xyz('abc.xyz'))
print(find_xyz('abcxyz'))
print(find_xyz('xyz'))
print(find_xyz('xyz.abc'))