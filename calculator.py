#calculator program
def add(a, b):
    return a + b

def subb(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divider(a, b):
    if b == 0:
        return "error! division by zero."
    return a / b


print("Calculator")
print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")

choice=int(input("Enter your choice(1 to 4):"))
num1=float(input("Enter the first number:"))
num2=float(input("enter the second number:"))

if choice == 1:
    print("Result:",add(num1, num2))
elif choice == 2:
    print("Result:",subb(num1, num2))
elif choice == 3:
    print("Result:",multiply(num1, num2))
elif choice == 4:
    print("Result:",divider(num1, num2))
else:
    print("invalid choice")


#other one


"""
def add(a, b):
    return a + b

def subb(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divider(a, b):
    if b == 0:
        return "error! division by zero."
    return a / b


print("Calculator")
print("+.Addition")
print("-.Substraction")
print("*.Multiplication")
print("/.Division")

choice=(input("Enter your choice(1 to 4):"))
num1=float(input("Enter the first number:"))
num2=float(input("enter the second number:"))

if choice == '+':
    print("Result:",add(num1, num2))
elif choice == '-':
    print("Result:",subb(num1, num2))
elif choice == '*':
    print("Result:",multiply(num1, num2))
elif choice == '/':
    print("Result:",divider(num1, num2))
else:
    print("invalid choice")"""
           
