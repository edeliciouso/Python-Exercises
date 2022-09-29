burger_price = int(input("Insert burger selling price: "))
soda_price = int(input("Insert soda selling price: "))
combo_meal_price = int(input("Insert combo meal price: "))

fixed_price = (burger_price + soda_price) - combo_meal_price
print("The fixed price is: $" + str(fixed_price))