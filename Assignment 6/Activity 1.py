# This programs changes your gross pay to weekly,
# montly, and anual pay


def calc_anual(weekly):
    anual = weekly * 52
    
    return anual


def calc_monthly(weekly):
    monthly = weekly * 4
    
    return monthly


def calc_pay(hours, rate):
    pay = hours * rate
    
    return pay


def calc_weekly(hours, rate):
    weekly = hours * rate * 7
    
    return weekly


def display_result(pay, weekly, monthly, anual):
    print("The employee gross pay is $" + str(pay) + "." + " The employee weekly pays is $" + str(weekly) + "." + " The employee montly pay is $" + str(monthly) + "." + " The employee anual pay is $" + str(anual) + ".")

    
def get_hours():
    print("Enter the number of hours")
    hours = float(input())
    
    return hours


def get_rate():
    print("Enter the hourly rate")
    rate = float(input())
    
    return rate


hours = get_hours()
rate = get_rate()
pay = calc_pay(hours, rate)
weekly = calc_weekly(hours, rate)
monthly = calc_monthly(weekly)
anual = calc_anual(weekly)
display_result(pay, weekly, monthly, anual)
