a = int(input("Enter the point of px: "))
b = int(input("Enter the point of py: "))
c = int(input("Enter the point of qx: "))
d = int(input("Enter the point of qy: "))

rx = 2 * (c - a)
ry = 2 * (d - b)

print("The point of r is: (" + str(rx) + "," + str(ry) + ")")