import sys

args = sys.argv

print(f"This is the name of the script {args[0]}")
print(f"Number of arguments : {len(args)}")

if len(args) > 1:
    print(f"Argument List : {args}")

