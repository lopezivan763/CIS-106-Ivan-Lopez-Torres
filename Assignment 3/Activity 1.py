# This program converts an input hourly pay rate to a weekly, montly and anual income

print("Enter the number of hours")

hours = float(input())

print("Enter the hourly pay rate")

payRate = float(input())

grossPay = hours * payRate

print("The employee gross pay is $" + str(grossPay))

monthly = grossPay * 4

yearly = grossPay * 52

print("The employee weekly pay is $" + str(grossPay) + ". The employee montly pay is $" + str(monthly) + ". The employee anual pay is $" + str(yearly) + ".")
