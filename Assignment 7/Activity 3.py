# This program ask the users if they would like to cheange 
# the miles int US measurements or metric measurements


def calc_centimeters(miles):
    centimeters = miles * 160934.4
    
    return centimeters


def calc_feet(miles):
    feet = miles * 5280

    return feet


def calc_inches(miles):
    inches = miles * 63360
    
    return inches


def calc_kilometers(miles):
    kilometers = miles * 1.609
    
    return kilometers


def calc_meters(miles):
    meters = miles * 1609.344
    
    return meters


def calc_yards(miles):
    yards = miles * 1760
    
    return yards


def display_centimeters(centimeters):
    print("The miles in centimeters are " + str(centimeters) + " centimeters")

    
def display_feet(feet):
    print("The miles into feet are " + str(feet) + " feet.")

    
def display_inches(inches):
    print("The miles into inches are " + str(inches) + " inches.")

    
def display_kilometers(kilometers):
    print("The miles into kilometers are " + str(kilometers) + " kilometers.")

    
def display_meters(meters):
    print("The miles into meters are " + str(meters) + " meters.")

    
def display_yards(yards):
    print("The miles into yards are " + str(yards) + " yards.")

    
def get_miles():
    print("Enter miles")
    miles = int(input())
    
    return miles


def get_choice():
    print("Do you want US measurements or metric measurements?")
    choice = input()
    
    return choice


def main():
    
    miles = get_miles()
    choice = get_choice()
    yards = calc_yards(miles)
    feet = calc_feet(miles)
    inches = calc_inches(miles)
    kilometers = calc_kilometers(miles)
    meters = calc_meters(miles)
    centimeters = calc_centimeters(miles)
    
    if choice == "US":
        display_yards(yards)
        display_feet(feet)
        display_inches(inches)
    else:
          
        if choice == "metric":
            display_kilometers(kilometers)
            display_meters(meters)
            display_centimeters(centimeters)
        else:
            print("Please enter if you want to convert to US measurements or metric measurements")
    
    
main()
