spam = ['apples', 'bananas', 'tofu', 'cats']

def addAnd(listValue):
    newString = ''
    for i in listValue:
        if listValue.index(i) == len(listValue) -1:
            newString += 'and ' + i
        else:
            newString += i + ', '
    return newString

print(spam)
print(addAnd(spam))
