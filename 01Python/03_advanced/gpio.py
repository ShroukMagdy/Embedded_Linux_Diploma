import os 

Register_bits = 8
Register_Value = "0b"
#func to take input from user
def Input_User():
    global Register_Value
    for i in range(Register_bits):
        Bit_Value = input(f"Please enter Bit {i} mode : ")
        if Bit_Value.lower() == "in":
           Register_Value+="0"
        elif Bit_Value.lower() == "out":
           Register_Value+="1"
        else:
            print("Wrong input Bit is set to default value in")
            Register_Value+="0"

#func to create the file
def Create_File():
    global Register_Value
    with open(os.path.join(os.getcwd()+"/InitGpio.c"),'w') as inputfile:
        inputfile.write("void Init_PORTA_DIR (void)\n\
                        {\n\
                            DDRA = "+Register_Value+";\n\
                        }")
        inputfile.close()

Input_User()
Create_File()