def calcFeet(miles):
    feet = miles * 5280
    
    return feet

def calcInches(miles):
    inches = miles * 63360
    
    return inches

def calcYards(miles):
    yards = miles * 1760
    
    return yards

def displayResult(miles, yards, feet, inches):
    print("The distance from miles in yards is " + str(yards) + " yards.")
    print("The distance from miles into feet is " + str(feet) + " feet.")
    print("The distance from miles to inches is " + str(inches) + " inches.")

def getMiles():
    print("Enter miles")
    miles = float(input())
    
    return miles

# Main
# This program calculates the distance from miles into yards, feet, and inches.
miles = getMiles()
yards = calcYards(miles)
feet = calcFeet(miles)
inches = calcInches(miles)
displayResult(miles, yards, feet, inches)
