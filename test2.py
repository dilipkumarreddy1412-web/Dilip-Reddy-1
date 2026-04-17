def binaryToDecimal(s):
 return int(str(s),2)

n=input("Enter the binary number:")
print("Equivalent Decimal Number:",binaryToDecimal(n))


def decimalToBinary(d):
  d=int(d,10)
  return bin(d)[2:]
n=input("enter the decimal number:")
print("equivalent binary number:",decimalToBinary(n))

