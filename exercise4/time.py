n = int(input("Enter the number of seconds: "))

hour = n // 3600

seconds = n % 3600

minutes = seconds // 60

seconds = n % 60

print("Result: " + str(hour) + ":" + str(minutes) + ":" + str(seconds))