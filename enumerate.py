import random



supplies = ['pens', 'staplers', 'flamethrowers', 'binders']

random.shuffle(supplies)

for index, item in enumerate(supplies):
    print('Index ' + str(index) + ' in supplies is: ' + item)

print(random.choice(supplies))

