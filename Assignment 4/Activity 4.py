# This is a basic program that
# turns dog years into human years


print("what is the name of the dog?")

name = input()

print("How old is " + str(name) + " in human years?")

age = float(input())

print(str(name) + " is " + str(age) + " years old in human years.")

print("What size is your dog?" " small medium, or large?")

size = input()

print(str(name) + " is a " + str(size) + " dog")
print('')
print("What type is your dog?")

type = input()

print(str(name) + " is a " + str(type) + ".")
print('')
print("7 human years equals 1 dog year.")
print('')

human = age / 7

print(str(name) + " is a " + str(size) + " dog.")
print('')
print(str(name) + " is a " + str(type) + ".")
print('')
print(str(name) + " is " + str(age) + " in human years.")
print('')
print(str(name) + " is " + str(human) + " years old in dog year.")