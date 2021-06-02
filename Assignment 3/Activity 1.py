# This program converts an input hourly pay rate to a weekly,
# montly and anual income.

print("Enter the number of hours")
hours = float(input())

print("Enter the hourly pay rate")
payRate = float(input())

grossPay = hours * payRate
monthly = grossPay * 4
yearly = grossPay * 52

print("The employee gross pay is $" + str(grossPay))
print("The employee weekly pay is $" + str(grossPay) +
    ". The employee monthly pay is $" + str(monthly) +
    ". The employee yearly pay is $" + str(yearly) + ".")
