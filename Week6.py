#----------------------------------------------------------------------------------------------------------------------
# Name: Week 6 Assignment
# Author: Wesley Wang
# Date: 2/19/2018
# Description: Read, modify, overwrite tasks listed in Todo.txt
#------------------------------------------------------------------------------------------------------------------------

# Declare variables
objFileName = "C:\_PythonClass\Todo.txt"
lstTable = []

class toDoFunctions(object):
    # Load data in Todo.txt into a list of dictionaries
    @staticmethod
    def readFile(filePath):
        objFile = open(filePath, "r")
        for row in objFile:
            strData = row.split(",")
            dicRow = {"Task": strData[0].strip(), "Priority": strData[1].strip()}
            lstTable.append(dicRow)
        objFile.close()

    # Display tasks and priorities in current list
    @staticmethod
    def showList():
        result = ""
        for item in lstTable:
            result += "Task: " + item["Task"].capitalize() + ", Priority : " + item["Priority"].capitalize() + "\n"
        return print(result)

    # Add or Remove items from the list
    @staticmethod
    def modifyList(task, priority, option):
        if(option == "add"):
            dicRow = {"Task": task, "Priority": priority}
            lstTable.append(dicRow)
            print("Item Saved!")
        elif(option == "remove"):
            for row in lstTable:
                if (str(row["Task"]).lower() == task.lower()):
                    lstTable.remove(row)
                    print("Task removed")

    # Overwrite Todo.txt with tasks in current list
    @staticmethod
    def saveToList(filePath):
        objFile = open(filePath, "w")
        for row in lstTable:
            objFile.write(str(row["Task"])+","+str(row["Priority"])+"\n")
        print("Tasks saved to ToDo.txt !")
        objFile.close()


# Load data from Todo.txt
toDoFunctions.readFile(objFileName)

# Display a menu of choices to the user
while(True):
    print ("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 4] - "))
    print()
    # Show current data
    if (strChoice.strip() == '1'):
        toDoFunctions.showList()
        continue
    # Add a new item
    elif(strChoice.strip() == '2'):
        strTask = str(input("What is your new task? : ")).capitalize()
        strPrior = str(input("What is the priority of your new task? (High/Low) : ")).capitalize()
        if(strPrior.lower() in ("high", "low")):
            toDoFunctions.modifyList(strTask, strPrior, "add")
        else:
            print("Please Enter A Correct Priority !!  (High/Low)")
        continue
    # Remove an existing item
    elif(strChoice == '3'):
        strRmvTask = str(input("What task do you want to remove? : "))
        toDoFunctions.modifyList(strRmvTask, "", "remove") #blank string as a filler for priority
        continue
    # Save data list current list to Todo.txt
    elif(strChoice == '4'):
        toDoFunctions.saveToList(objFileName)
        continue
    elif (strChoice == '5'):
        print("Program ended!")
        break #and Exit the program
    else:
        print("Please Enter A Correct Option!!")
        continue
