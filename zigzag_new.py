import time
def zigzag():
    while True:
        for i in range(1,20):
            print(' ' * i, end='')
            print("*" * 10)
            time.sleep(0.5)

        for j in range(20,0,-1):
            print(' ' * j, end='')
            print("*" *10)
            time.sleep(0.5)

zigzag()



# print('hi', end='')
# print('bye')


# print('.', end='')
# print('.')