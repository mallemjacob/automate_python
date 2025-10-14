def spam(divideBy):
    return 42 / divideBy
    
print(spam(2))
print(spam(12))
try:
    print(spam(0))
except ZeroDivisionError:
    print('no zero')
print(spam(1))