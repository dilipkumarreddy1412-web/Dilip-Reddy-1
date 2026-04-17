
#to cheack weather the number is divisible by 2 and 3
num = int(input("enter a number:"))
if num % 2 == 0 and num % 3 == 0:
    print("The number is divisible by both 2 and 3.")
else:
    print("The number is not divisible by both 2 and 3.")



#to cheack weather the number is divisible by 2 and 3
def cheack_divisibility(num):
    if num % 2 == 0 and num % 3 == 0:
        return "The number is divisible by both 2 and 3."
    else:
        return"The number is not divisible by both 2 and 3."
num = int(input("enter a number:"))
print(cheack_divisibility(num))


#to print the sum of the first N natural numbers 
n = int(input("enter a number:"))
s = 0
for i in range (1, n + 1,1):
    s += i
print("sum of first",n,"naturam number is :",s)


#to print the sum of the first N natural numbers 
def sum_natural(n):
    return n * (n + 1)//2

n = int(input("enter a number:"))
print("sum of first",n,"naturam number is :",sum_natural(n))


#to print the sum of the first N natural numbers 
def sum_n(n):
    if n == 0:
        return 0
    else:
        return n + sum_n(n - 1)

n = int(input("enter a number:"))
print("sum =",sum_n(n))

