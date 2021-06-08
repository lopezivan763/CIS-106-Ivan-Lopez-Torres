# This program changes human years
# to dog years

def calcAge(human):
    age = float(human) / 7

    return age

def displayResult(name, human, age):
    print(name + " is " + str(age) + " years old in dog years.")

def getHuman():
    print("Enter the dog's age in human years")
    human = int(input())

    return human

def getName():
    print("Enter the dog's name")
    name = input()

    return name

def main():
    name = getName()
    human = getHuman()
    age = calcAge(human)
    displayResult(name, human, age)

main()
