import numpy as np
x = np.array([1,2,3,4,5])
y = np.array([2,4,5,4,5])
m , b =np.polyfit(x, y, 1)

print("slop=",m)
print("intercept=",b)
print("equation: y =", m, "x +", b)
