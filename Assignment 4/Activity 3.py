# This program calculates miles
# to yard, feet, and inches

print("What is the distance in miles?")
miles = float(input())

yards = miles * 1760
feet = miles * 5280
inches = miles * 63360

print("The distance is " + str(miles) + " miles.")
print("The distance from miles to yards is " + str(yards) + " yards.")
print("The distance from miles to feet is " + str(feet) + " feet.")
print("The distance from miles to inches is " + str(inches) + " inches.")
