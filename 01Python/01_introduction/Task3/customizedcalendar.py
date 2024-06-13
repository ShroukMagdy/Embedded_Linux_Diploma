import calendar
import sys

#input from user
GivenYear = input("Please enter the year (e.g., 2017):")

#Check the input
try:
    GivenYear = int(GivenYear)
    if not (GivenYear > 0 ) :
        print("ERROR: Your input is not a valid year")
        sys.exit()
except ValueError:
    print("ERROR: Your input is not a number")
    sys.exit()

GivenMonth = input("Please enter the month (e.g., 8):")

#Check the input
try:
    GivenMonth = int(GivenMonth)
    if not (GivenMonth > 0 and GivenMonth < 13) :
        print("ERROR: Your input is not a valid month")
        sys.exit()
except ValueError:
    print("ERROR: Your input is not a number")
    sys.exit()

try:
    print(calendar.month(GivenYear,GivenMonth))
except ValueError as e:
    print(f"Error: {e}")
