# This program converts an input hourly pay rate to a weekly, montly and anual income
print("Enter the number of hours")
hours = float(input())
print("Enter the hourly pay rate")
payRate = float(input())
grossPay = hours * payRate
print("The employee gross pay is $" + str(grossPay))
weekly = hours * payRate * 7
montly = weekly * 4
anual = weekly * 52
print("The employee weekly pay is $" + str(weekly) + ". The employee montly pay is $" + str(montly) + ". The employee anual pay is $" + str(anual) + ".")
