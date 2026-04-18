import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
x = np.array([1,2,3,4,5]).reshape(-1,1)
y = np.array([2,4,5,4,5])
ob = LinearRegression()
ob.fit(x ,y)
y_pred = ob.predict(x)
mae = mean_absolute_error(y, y_pred)
print("mean absolute error", mae)
