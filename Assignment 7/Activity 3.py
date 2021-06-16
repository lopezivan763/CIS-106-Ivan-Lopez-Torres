def calcCentimeters(miles):
    centimeters = miles * 160934.4
    
    return centimeters

def calcFeet(miles):
    feet = miles * 5280
    
    return feet

def calcInches(miles):
    inches = miles * 63360
    
    return inches

def calcKilometers(miles):
    kilometers = miles * 1.609
    
    return kilometers

def calcMeters(miles):
    meters = miles * 1609.344
    
    return meters

def calcYards(miles):
    yards = miles * 1760
    
    return yards

def displayCentimeters(centimeters):
    print("The miles in centimeters are " + str(centimeters) + " centimeters")

def displayFeet(feet):
    print("The miles into feet are " + str(feet) + " feet.")

def displayInches(inches):
    print("The miles into inches are " + str(inches) + " inches.")

def displayKilometers(kilometers):
    print("The miles into kilometers are " + str(kilometers) + " kilometers.")

def displayMeters(meters):
    print("The miles into meters are " + str(meters) + " meters.")

def displayYards(yards):
    print("The miles into yards are " + str(yards) + " yards.")

def getMiles():
    print("Enter miles")
    miles = int(input())
    
    return miles

def getChoice():
    print("Do you want US measurements or metric measurements?")
    choice = input()
    
    return choice

# Main
# This program ask the users if they would like to cheange the miles int US measurements or metric measurements
miles = getMiles()
choice = getChoice()
yards = calcYards(miles)
feet = calcFeet(miles)
inches = calcInches(miles)
kilometers = calcKilometers(miles)
meters = calcMeters(miles)
centimeters = calcCentimeters(miles)
if choice == "us":
    displayYards(yards)
    displayFeet(feet)
    displayInches(inches)
else:
    if choice == "metric":
        displayKilometers(kilometers)
        displayMeters(meters)
        displayCentimeters(centimeters)
    else:
        print("Please selec us or metric measurements")
