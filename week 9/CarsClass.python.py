class Cars:
    company = "Unknown"
    price = 0
    color = "Unknown"
    def display(self):
        print(f"The Brand is ",self.company)
        print(f"The price is ",self.price)
        print(f"The color is ",self.color)
        print("-" * 30)


car1 = Cars()
car1.company = "Audi"
car1.price = 5000000
car1.color = "Red"

car2 = Cars()
car2.company = "BMW"
car2.price = 6000000
car2.color = "Black"

car3 = Cars()
car3.company = "Benz"
car3.price = 7000000
car3.color = "Yellow"

print("CAR 1 DETAILS \n")
car1.display()
print("CAR 2 DETAILS \n")
car2.display()
print("CAR 3 DETAILS \n")
car3.display()
