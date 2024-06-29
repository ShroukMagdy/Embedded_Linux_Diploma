import pandas as pd
import re
import os

Header_func = []
Header_func_ID = []
#func to parse header file
def Parse_Header():
    global Header_func,Header_func_ID
    pattern = re.compile("^(void|int|struct|char|enum|bool|Dio_PortLevelType|Dio_LevelType).+;$")

    with open(os.path.join(os.getcwd(),"Dio.h"),'r')as inputfile:
        for i, line in enumerate(inputfile):
            for match in re.finditer(pattern, line):
                # print('Found on line %s: %s' % (i+1, match.group()))
                Header_func.append(match.group())
        
        for i in range(len(Header_func)):
            Header_func_ID.append(f"IDX00{i}")

#func to write data in excel file
def Write_Excel():
    global Header_func,Header_func_ID
    data = {
        'function' : Header_func,
        'Index' : Header_func_ID
    }
    df = pd.DataFrame(data)
    df.to_excel('functions.xlsx',index=False)
    
Parse_Header()
Write_Excel()