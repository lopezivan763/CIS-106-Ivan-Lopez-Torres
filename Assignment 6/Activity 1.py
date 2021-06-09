def calcAnual(weekly):
    anual = weekly * 52
    
    return anual

def calcMonthly(weekly):
    monthly = weekly * 4
    
    return monthly

def calcPay(hours, rate):
    pay = hours * rate
    
    return pay

def calcWeekly(hours, rate):
    weekly = hours * rate * 7
    
    return weekly

def displayResult(pay, weekly, monthly, anual):
    print("The employee gross pay is $" + str(pay) + "." + " The employee weekly pays is $" + str(weekly) + "." + " The employee montly pay is $" + str(monthly) + "." + " The employee anual pay is $" + str(anual) + ".")

def getHours():
    print("Enter the number of hours")
    hours = float(input())
    
    return hours

def getRate():
    print("Enter the hourly rate")
    rate = float(input())
    
    return rate

# Main
hours = getHours()
rate = getRate()
pay = calcPay(hours, rate)
weekly = calcWeekly(hours, rate)
monthly = calcMonthly(weekly)
anual = calcAnual(weekly)
displayResult(pay, weekly, monthly, anual)
