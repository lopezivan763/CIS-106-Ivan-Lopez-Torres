# This program ask the users if they want to calculate their 
# age into months, days, hours, or seconds.


def calcDays(age):
    days = age * 365
    
    return days

def calcHours(age):
    hours = age * 8760
    
    return hours

def calcMonths(age):
    months = age * 12
    
    return months

def calcSeconds(age):
    seconds = age * 31536000
    
    return seconds

def displayDays(days):
    print("Your age in days is " + str(days) + " days.")

def displayHours(hours):
    print("Your age in hours is " + str(hours) + " hours.")

def displayMonths(months):
    print("Your age in months is " + str(months) + " months.")

def displaySeconds(seconds):
    print("Your age in seconds is " + str(seconds) + " seconds.")

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
    months = calcMonths(age)
    days = calcDays(age)
    hours = calcHours(age)
    seconds = calcSeconds(age)
if choice == "months":
    displayMonths(months)
else:
    if choice == "days":
        displayDays(days)
    else:
        if choice == "hours":
            displayHours(hours)
        else:
            if choice == "seconds":
                displaySeconds(seconds)
            else:
                print("Please select if you want your age to be display in months, days, hours, or seconds")
                
main()
