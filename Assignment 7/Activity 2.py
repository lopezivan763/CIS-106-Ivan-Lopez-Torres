# This program ask the users if they want to calculate 
# their age into months, days, hours, or seconds.


def calcDays(age):
    days = age * 365
    print("Your age in days is " + str(days) + " days.")
    
    return days

def calcHours(age):
    hours = age * 8760
    print("Your age in hours is " + str(hours) + " hours.")
    
    return hours

def calcMonths(age):
    months = age * 12
    print("your age in months is" + str(months) + " months.")
    
    return months

def calcSeconds(age):
    seconds = age * 31536000
    print("Your age in seconds is " + str(seconds) + " seconds.")
    
    return seconds

def getAge():
    print("Enter your age")
    age = float(input())
    
    return age

def getChoice():
    print("Would you like to know yor age in months, days, hours, or seconds?")
    choice = input()
    
    return choice

def main():
    age = getAge()
    choice = getChoice()
    if choice == "months":
    calcMonths(age)
else:
    if choice == "days":
        calcDays(age)
    else:
        if choice == "hours":
            calcHours(age)
        else:
            if choice == "seconds":
                calcHours(age)
