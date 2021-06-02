# program that calculates the age of the user to years months, days, etc.
\n
print("How old are you?")
\n
age = float(input())
\n
print("The users age is " + str(age) + " year's old.")
\n
months = age * 12
\n
days = age * 365
\n
hours = age * 8760
\n
seconds = age * 31536000
\n
print("The user age in months is " + str(months) + " months.")
\n
print("The user age in days is " + str(days) + " days.")
\n
print("The user age in hours is " + str(hours) + " hours.")
\n
print("The user age in seconds is " + str(seconds) + " seconds.")
