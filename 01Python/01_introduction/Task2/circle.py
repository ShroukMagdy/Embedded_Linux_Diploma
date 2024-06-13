import sys

pi = 3.14159

#input from user
GivenNumber = input("Please enter the radius (e.g., 3 or 3.15):")

#Check the input
try:
    GivenNumber = float(GivenNumber)
except ValueError:
    print("ERROR: Your input is not a number")
    sys.exit()

print("The area of the circle of radius ",str(GivenNumber)," is ",str(pi*(GivenNumber**2)))
