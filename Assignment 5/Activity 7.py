# This program changes human years
# to dog years

def calc_age(human):
    age = float(human) / 7

    return age

def display_result(name, human, age):
    print(name + " is " + str(age) + " years old in dog years.")

def get_human():
    print("Enter the dog's age in human years")
    human = int(input())

    return human

def get_name():
    print("Enter the dog's name")
    name = input()

    return name

def main():
    name = get_name()
    human = get_human()
    age = calc_age(human)
    display_result(name, human, age)

main()
