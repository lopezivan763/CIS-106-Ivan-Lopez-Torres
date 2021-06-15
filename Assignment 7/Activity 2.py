# This program ask the users if they want to calculate their 
# age into months, days, hours, or seconds.


def calc_days(age):
    days = age * 365
    
    return days

def calc_hours(age):
    hours = age * 8760
    
    return hours

def calc_months(age):
    months = age * 12
    
    return months

def calc_seconds(age):
    seconds = age * 31536000
    
    return seconds

def display_days(days):
    print("Your age in days is " + str(days) + " days.")

def display_hours(hours):
    print("Your age in hours is " + str(hours) + " hours.")

def display_months(months):
    print("Your age in months is " + str(months) + " months.")

def display_seconds(seconds):
    print("Your age in seconds is " + str(seconds) + " seconds.")

def get_age():
    print("Enter your age")
    age = float(input())
    
    return age

def get_choice():
    print("Would you like to know your age in (M)onths, (D)ays, (H)ours, or (S)econds?")
    choice = input()
    
    return choice

def main():
    age = get_age()
    choice = get_choice()
    months = calc_months(age)
    days = calc_days(age)
    hours = calc_hours(age)
    seconds = calc_seconds(age)

    if choice == "M":
        display_months(months)
    else:
        
        if choice == "D":
            display_days(days)
        else:
        
            if choice == "H":
                display_hours(hours)
            else:
        
                if choice == "S":
                    display_seconds(seconds)
                else:
                    print("Please select if you want your age to be display in months, days, hours, or seconds")
                
main()
