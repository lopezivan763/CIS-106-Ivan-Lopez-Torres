# This is a program that calculates the age of the user to years months, days, etc.

print("How old are you?")
age = float(input())
print("The users age is " + str(age) + " year's old.")
print()
months = age * 12
days = age * 365
hours = age * 8760
seconds = age * 31536000
print("The user age in months is " + str(months) + " months.")
print()
print("The user age in days is " + str(days) + " days.")
print()
print("The user age in hours is " + str(hours) + " hours.")
print()
print("The user age in seconds is " + str(seconds) + " seconds.")
