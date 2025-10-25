class Mobile:
    def __init__(self, argmodel, argdisplay, argprice):
        # attributes
        self.model = argmodel
        self.display = argdisplay
        self.price = argprice
        self.audioJack = False
    
    #methods
    def calling(self):
        return f'calling from.. {self.model}'

    def browsing(self):
        return f'browsing from.. {self.model}. It costs {self.price} rupees.'
    
    def changeAudioJack(self, isAudioAvailable=False):
        self.audioJack = isAudioAvailable
    

samsung_10 = Mobile('Samsung 10', 6.2, 80)
iphone_15 = Mobile('Iphone 15', 5.8, 90)
one_plus = Mobile('Oneplus Nord', 6.4, 50)

print(samsung_10.model)
print(iphone_15.model)
print(one_plus.model)

print(samsung_10.calling())

samsung_10.changeAudioJack(True)
iphone_15.changeAudioJack()
one_plus.changeAudioJack(True)

print(f'Audio jack available for samsung s10: {samsung_10.audioJack}')
print(f'Audio jack available for iphone 15: {iphone_15.audioJack}')
print(f'Audio jack available oneplus: {one_plus.audioJack}')


# def hello(name,age):
#     newdict = {"name":name, "age":age, "gender":'M'}
#     return newdict

# print(hello('val',18))
# print(hello('bhi',19))
# print(hello('jul',20))