filename=r"m:\1st semester\python\student.txt"

def write_student():
    student=[
        "111,prasad,90,85\n",
        "112,venky,70,10\n",
        "113,likith,20,16\n"
        ]
    with open(filename,"w")as file:
        file.writelines(student)
    print("simple student data written to file.\n")


def read_student():
    print("\n student records")
    try:
        with open(filename,"r")as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("file not found, please write data first.")

def append_student():
    roll=input("enter a roll number:")
    name=input("enter a name:")
    age=input("enter a age:")
    marks=input("enter a marks:")

    with open(filename,"a")as file:
        file.write(f"{roll}, {name}, {age}, {marks}\n")
    print("student data append successfully.\n")


while True:
    print("1.write sample student data")
    print("2.read student data")
    print("3.append new student data")
    print("4.exit")

    choice=input("enter your choice")

    if choice=="1":
        write_student()
    elif choice=="2":
        read_student()
    elif choice=="3":
        append_student()
    elif choice=="4":
        print("exiting program")
        break
    else:
        print("invalid choice! please try again")
        
    
