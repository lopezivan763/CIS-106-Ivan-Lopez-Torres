# This is a basic program that
# turns dog years into human years

print("what is the name of the dog?")
name = input()

print("How old is " + str(name) + " in human years?")
age = float(input())

human = age / 7

print(str(name) + " is " + str(age) + " years old in human years.")
print("7 human years equals 1 dog year.")
print(str(name) + " is " + str(human) + " years old in dog year.")
