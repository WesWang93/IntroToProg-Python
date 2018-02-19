#-------------------------------------------------#
# Title: Working with Dictionaries
# Dev:   RRoot
# Date:  July 16, 2012
# ChangeLog: (Who, When, What)
#   RRoot, 11/02/2016, Created starting template
#   Wesley Wang, Assignment 5
#https://www.tutorialspoint.com/python/python_dictionary.htm
#-------------------------------------------------#

objFileName = "C:\_PythonClass\Week5\Todo.txt"
strData = ""
dicRow = {}
lstTable = []

# Step 1 - Load data from a file
    # When the program starts, load each "row" of data 
    # in "ToDo.txt" into a python Dictionary.
    # Add the each dictionary "row" to a python list "table"

objFile = open(objFileName, "r")
for row in objFile:
    strData = row.split(",")
    dicRow = {"Task" : strData[0].strip(), "Priority" : strData[1].strip()}
    lstTable.append(dicRow)
objFile.close()
# Step 2 - Display a menu of choices to the user
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
    print()#adding a new line

    # Step 3 -Show the current items in the table
    if (strChoice.strip() == '1'):
        for item in lstTable:
            print("Task: " + item["Task"].capitalize() + ", Priority : " + item["Priority"].capitalize())
        continue
    # Step 4 - Add a new item to the list/Table
    elif(strChoice.strip() == '2'):
        strTask = str(input("What is your new task? : ")).capitalize()
        strPrior = str(input("What is the priority of your new task? (High/Low) : ")).capitalize()
        if(strPrior.lower() in ("high", "low")):
            dicRow = {"Task" : strTask, "Priority" : strPrior}
            lstTable.append(dicRow)
            print("Item Saved!")
        else:
            print("Please Enter A Correct Priority !!  (High/Low)")
        continue
    # Step 5 - Remove a new item to the list/Table
    elif(strChoice == '3'):
        strRmvTask = str(input("What task do you want to remove? : "))
        for row in lstTable:
            if(str(row["Task"]).lower() == strRmvTask.lower()):
                lstTable.remove(row)
                print("Task removed")
        continue
    # Step 6 - Save tasks to the ToDo.txt file
    elif(strChoice == '4'):
        objFile = open(objFileName, "w")
        for row in lstTable:
            objFile.write(str(row["Task"])+","+str(row["Priority"])+"\n")
        print("Tasks saved to ToDo.txt !")
        objFile.close()
        continue
    elif (strChoice == '5'):
        print("Program ended!")
        break #and Exit the program
    else:
        print("Please Enter A Correct Option!!")
        continue

