# This program turns your age into months, days, hours, and seconds.
print("enter your age")
age = int(input())
months = age * 12
days = age * 365
hours = age * 8760
seconds = age * 31536000
print("Your age in months is " + str(months) + " months.")
print("Your age in days is " + str(days) + " days.")
print("Your age in hours is" + str(hours) + " hours.")
print("Your age in seconds is" + str(seconds) + " seconds.")
