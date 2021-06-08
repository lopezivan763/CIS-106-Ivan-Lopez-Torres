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

def displayResult(age, months, days, hours, seconds):
    print(" Your age in months is " + str(months) + " months." + " Your age in days is " + str(days) + " days." + " Your age in hours is " + str(hours) + " hours." + " Your age in seconds is " + str(seconds) + " seconds.")

def getAge():
    print("Enter your age")
    age = float(input())
    
    return age

# Main
# This program changes your age to months, days, hours, and seconds.
age = getAge()
months = calcMonths(age)
days = calcDays(age)
hours = calcHours(age)
seconds = calcSeconds(age)
displayResult(age, months, days, hours, seconds)
