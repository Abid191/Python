class car: 
    def __init__(self,name,price,color):     #constructor create #__inint__ constructor
        self.name = name         #variable declare 
        self.price = price         #variable declare 
        self.color = color         #variable declare 

    def details(self):
        print('car name : ',self.name,'car price : ',self.price,'car color : ',self.color)   #(another method) 

car1 = car('bmw ,','4000$ ,','blue')
car1.details()                   #(object)  