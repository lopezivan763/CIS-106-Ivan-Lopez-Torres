# This programs changes your gross pay to weekly,
# montly, and anual pay


def calc_anual(pay):
    anual = pay * 52
    
    return anual


def calc_monthly(pay):
    monthly = pay * 4
    
    return monthly


def calc_pay(hours, rate):
    pay = hours * rate
    
    return pay


def calc_weekly(hours, rate):
    weekly = hours * rate * 5
    
    return weekly


def display_result(pay, weekly, monthly, anual):
    print("The employee gross pay is $" + str(pay) + ".")  
    print("The employee weekly pays is $" + str(weekly) + ".") 
    print("The employee monthly pay is $" + str(monthly) + ".")
    print("The employee yearly pay is $" + str(anual) + ".")

    
def get_hours():
    print("Enter the number of hours")
    hours = float(input())
    
    return hours


def get_rate():
    print("Enter the hourly rate")
    rate = float(input())
    
    return rate


def main():
    hours = get_hours()
    rate = get_rate()
    pay = calc_pay(hours, rate)
    weekly = calc_weekly(hours, rate)
    monthly = calc_monthly(pay)
    anual = calc_anual(pay)
    display_result(pay, weekly, monthly, anual)


main()
