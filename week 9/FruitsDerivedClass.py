class Fruits:
    def eat(self):
        print("we can eat fruits")
class Orange(Fruits):
    pass
class Apple(Fruits):
    def eat(self):
        print("Apple is sweet")
org1=Orange()
app1=Apple()
org1.eat()
app1.eat()
