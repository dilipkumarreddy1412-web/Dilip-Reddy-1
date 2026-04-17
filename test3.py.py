def arithematic(n1,n2):
    z=n1+n2
    z1=n1-n2
    z2=n1*n2
    z3=n1/n2
    return z,z1,z2,z3

a=int(input("enter a value:"))
b=int(input("enter another value:"))
print(arithematic(a,b))
