import numpy as np
x=[1,2,3,4,5]
y=[2,4,5,4,5]
n=len(x)
sum_x = sum(x)
sum_y = sum(y)
print("sum_x=",sum_x)
print("sum_y=",sum_y)
sum_xy =0
sum_x2 =0
for i in range(n):
    sum_xy += x[i] * y[i]
    sum_x2 += x[i] * x[i]
print("sum_xy=",sum_xy)
print("sum_x2=",sum_x2)
m=(n * sum_xy - sum_x * sum_y)/(n * sum_x2 - sum_x**2)
b=(sum_y - m * sum_x) / n
print("slop (m) =",m)
print("intercept (b) =",b)
print("\n regression equation:")
print("y =",m, "x +", b)
