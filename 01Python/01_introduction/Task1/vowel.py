import sys

#declare vowels
Vowels = ('a','e','i','o','u')

#input from user
GivenLetter = input("Please enter your letter (e.g., h):")

#Check the input
if not GivenLetter.isalpha():
    print("ERROR: Your input is not a valid string format")
    sys.exit()

if not len(GivenLetter) == 1:
    print("ERROR: Your input is not a single letter")
    sys.exit()

GivenLetter = GivenLetter.lower()
VowelFlag = False
for iterator in Vowels :
    if iterator == GivenLetter :
        VowelFlag = True
        break

if VowelFlag == False : 
    print("Your input is not a vowel")
else :
    print("Your input is a vowel")

