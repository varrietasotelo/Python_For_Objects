'''
item1 = "prhone"
item1_price = 100
item1_quantity = 5
item1_price_total = item1_price * item1_quantity


print(type(item1))
print(type(item1_price))
print(type(item1_quantity))
print(type(item1_price_total))

#Ejercicio inicial del video visto en clase 

'''

class Item:
    def calculate_total_price(self, x, y):
        return x * y

#recordar: siempre colocar nombres especificos a las variables, X y Y no es aceptable. 
#en el caso de item1, la X hara referencia a item1.price y la Y hara referencia a item1.quantity 

item1 = Item()
item1.name = "Phone" 
item1.price = 100
item1.quantity = 5
print(item1.calculate_total_price(item1.price, item1.quantity))

random_str = "aaa"
print(random_str.upper())

item2 = Item()
item2.name = "Laptop" 
item2.price = 1000
item2.quantity = 3
print(item1.calculate_total_price(item2.price, item2.quantity))