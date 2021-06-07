def calcDays():
    days = enterAge() * 360
    print("Your age in days is " + str(days) + " days")
    
    return days

def calcHours():
    hours = enterAge() * 8760
    print("Your age in hours is " + str(hours) + " hours")
    
    return hours

def calcMonths():
    months = enterAge() * 12
    print("your age in months is " + str(months))
    
    return months

def calcSeconds():
    seconds = enterAge() * 31536000
    print("Your age in seoconds is " + str(seconds) + " seconds")
    
    return seconds

def enterAge():
    age = int(input())
    
    return age

def results():
    print("Your age in months is " + str(calcMonths()) + " months. " + " Your age in days is " + str(calcDays()) + " days." + "Your age in hours is " + str(calcHours()) + " hours." + " Your age in seconds is " + str(calcSeconds()) + " seconds.")

# Main
# This program coverts your age to months, days, hours, and seconds
print("Please enter your age")
results()
