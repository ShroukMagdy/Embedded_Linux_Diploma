import sys
import ast

#Let the user write the input list
GivenList=input("Please enter your list (e.g., [1, 2, 3, 4]):")

# Convert the input string to a list
try:
    GivenList = ast.literal_eval(GivenList)
except (ValueError, SyntaxError):
    print("ERROR: Your input is not a valid list format")
    sys.exit()

#Check the input
if not isinstance(GivenList, list):
    print("ERROR : Your input is not a list")
    sys.exit()

#count no. 4
counter=0
for iterator in GivenList:
    if iterator == 4:
        counter+=1

if counter == 0:
    print("no. 4 is not in your list")
else:
    print("no. 4 in your list is repeated "+ str(counter) + " times")