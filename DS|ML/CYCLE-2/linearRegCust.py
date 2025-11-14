import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# ---- Dataset ----
x = np.array([95, 85, 80, 70, 60]).reshape(-1, 1)
y = np.array([85, 95, 70, 65, 70])

# ---- Train Linear Regression ----
model = LinearRegression()
model.fit(x, y)

# ---- Prediction for xi = 80 ----
pred = model.predict([[80]])
print("Predicted Statistics Grade:", pred[0])

# ---- Accuracy (Using same X and y since dataset is small) ----
y_pred_all = model.predict(x)

print("Coefficient (Slope):", model.coef_)
print("Mean Squared Error:", mean_squared_error(y, y_pred_all))
print("R2 Score:", r2_score(y, y_pred_all))

# ---- Plot ----
plt.scatter(x, y, color='black')
plt.plot(x, model.predict(x), color='blue')
plt.scatter([80], pred, color='red')
plt.show()
