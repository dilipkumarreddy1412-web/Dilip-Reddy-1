import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
x = np.array([1,2,3,4,5]).reshape(-1,1)
y = np.array([2,4,5,4,5])
ob = LinearRegression()
ob.fit(x ,y)
y_pred = ob.predict(x)
plt.scatter(x, y)
plt.plot(x, y_pred)

plt.xlabel("x values")
plt.ylabel("y values")
plt.title("Least Squares Linear Regression")
plt.show()
