bill = float(input("Insert the total bill here: $"))
people = float(input("Insert the amount of people here: "))
tips = float(input("Insert the tips here: $"))

tips_in_dollars = (tips / 100) * bill
total_all = bill + tips_in_dollars
total_per_people = total_all / people
tip_per_people = tips_in_dollars / people

print("The amount of tip per person is $" + str(tip_per_people) + " and the total amount per person is $" + str(total_per_people) + ".")
