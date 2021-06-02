# program that calculates the age of the user to years months, days, etc.
print("How old are you?" + ("\n"))
print()
age = float(input())
print("The users age is " + str(age) + " year's old." + ("\n"))
print()
months = age * 12
days = age * 365
hours = age * 8760
seconds = age * 31536000
print()
print("The user age in months is " + str(months) + " months." + ("\n"))
print()
print("The user age in days is " + str(days) + " days." + ("\n"))
print()
print("The user age in hours is " + str(hours) + " hours." + ("\n"))
print()
print("The user age in seconds is " + str(seconds) + " seconds." + ("\n"))
