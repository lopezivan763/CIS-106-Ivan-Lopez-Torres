# This is a basic program that
# turns dog years into human years


print("what is the name of the dog?")

name = input()

print("How old is " + str(name) + "?")

age = float(input())

print(str(name) + " is " + str(age) + " years old.")

print("1 dog year equals to 7 human year.")

human = age * 7

print(str(name) + " is " + str(human) + " in human years.")