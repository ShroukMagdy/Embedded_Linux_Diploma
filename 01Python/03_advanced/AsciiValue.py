import sys 

try:
    var = input("Please enter a charachter : ")
    print(ord(var))
except Exception as e:
    print(f"Error: {e}")
    sys.exit()