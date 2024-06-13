import os

#print all environment variables
print("Here is all the environment variables")
for key, value in os.environ.items():
    print(f"{key} = {value}")

print("Here is the OS var = ",str(os.environ.get('OS',"Not Set")))
print("Here is the PATH var = ",str(os.environ.get('PATH',"Not Set")))