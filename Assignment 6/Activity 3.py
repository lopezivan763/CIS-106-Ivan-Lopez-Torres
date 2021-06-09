# This program calculates the distance from miles into yards, feet, and inches.


def calc_feet(miles):
    feet = miles * 5280
    
    return feet


def calc_inches(miles):
    inches = miles * 63360
    
    return inches


def calc_yards(miles):
    yards = miles * 1760
    
    return yards


def display_result(miles, yards, feet, inches):
    print("The distance from miles in yards is " + str(yards) + " yards.")
    print("The distance from miles into feet is " + str(feet) + " feet.")
    print("The distance from miles to inches is " + str(inches) + " inches.")


def get_miles():
    print("Enter miles")
    miles = float(input())
    
    return miles


def main():
    miles = get_miles()
    yards = calc_yards(miles)
    feet = calc_feet(miles)
    inches = calc_inches(miles)
    display_result(miles, yards, feet, inches)
    

main()
