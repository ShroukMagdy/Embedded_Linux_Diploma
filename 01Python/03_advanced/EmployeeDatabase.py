#class of employee
class employee:
    Name = ""
    Job = ""
    Salary = 0
    UniqueID = 0
    def __init__(self,name,job,salary,uniqueID):
        self.Name = name
        self.Job = job
        self.Salary = salary
        self.UniqueID = uniqueID


ListEmployees = []

#check employee exists
def CheckEmployee(ID):
    global ListEmployees
    EmployeeFound = False
    if len(ListEmployees) > 0:
        for i in range(len(ListEmployees)):
            if ListEmployees[i].UniqueID == ID:
                EmployeeFound = True
                return EmployeeFound,i

    return EmployeeFound,0

#add new employee
def AddEmployee():
    global ListEmployees
    ID = input("Please enter employee ID : ")
    Found,index = CheckEmployee(ID)
    if Found:
        print("Employee already exists in the database")
    else:
        Name = input("Please enter employee name : ")
        Job = input("Please enter employee job : ")
        Salary = input("Please enter employee salary : ")
        ListEmployees.append(employee(Name,Job,Salary,ID))

#print employee data
def PrintEmployee():
    global ListEmployees
    ID = input("Please enter employee ID : ")
    Found,index = CheckEmployee(ID)
    if Found:
        print("Employee exists in the database")
        print(f"Employee Name = {ListEmployees[index].Name}")
        print(f"Employee Job = {ListEmployees[index].Job}")
        print(f"Employee Salary = {ListEmployees[index].Salary}")
    else:
        print("Employee does not exist in the database")
#remove employee from the system
def RemoveEmployee():
    global ListEmployees
    ID = input("Please enter employee ID : ")
    Found,index = CheckEmployee(ID)
    if Found:
        print("Employee exists in the database")
        del ListEmployees[index]
        print("Employee is removed")
    else:
        print("Employee does not exist in the database")  

#update employee data
def UpdateEmployee():
    global ListEmployees
    ID = input("Please enter employee ID : ")
    Found,index = CheckEmployee(ID)
    if Found:
        print("Employee exists in the database")
        Name = input("Please enter employee name : ")
        Job = input("Please enter employee job : ")
        Salary = input("Please enter employee salary : ")
        ListEmployees[index].Name = Name
        ListEmployees[index].Job = Job
        ListEmployees[index].Salary = Salary

    else:
        print("Employee does not exist in the database")

#func to control database
def UpdateDatabase():
    print("Welcome to the employee database")
    option = 0
    while option != 5:
        option = int(input("To add new employee enter 1\nTo print employee data enter 2\nTo remove employee data enter 3\nTo update employee data enter 4\nTo exit enter 5\nyour option is : "))
        if option == 1:
            AddEmployee()

        elif option == 2:
            PrintEmployee()
        elif option == 3:
            RemoveEmployee()
        elif option == 4:
            UpdateEmployee()
    print("DataBase Update done")

UpdateDatabase()
    
    
