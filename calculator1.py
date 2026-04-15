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

operations = {
    1: add,
    2: subb,
    3: multiply,
    4: divider
}
print("Calculator")
print("1.Add")
print("2.Sub")
print("3.Multiply")
print("4.Divider")

choice=int(input("Enter your choice(1 to 4):"))

if choice in operations:
    x = float(input("enter the first number:"))
    y = float(input("enter the second number:"))

    result = operations[choice](x, y)
    print("result:",result)
else:
    print("invalid choice")

           
