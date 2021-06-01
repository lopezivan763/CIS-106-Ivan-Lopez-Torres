# This program converts an input Fahrenheit temperature to Celsius.
print("Enter the Fahrenheit temperature")
fahrenheit = float(input())
celsius = (fahrenheit - 32) * 5 / 9
print(str(fahrenheit) + "º Fahrenheit is " + str(celsius) + "º Celsius")
