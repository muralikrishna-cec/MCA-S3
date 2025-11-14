from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score
import matplotlib.pyplot as plt

X,y=load_diabetes(return_X_y=True)

X=X[:,[2]]

x_train,x_test,y_train,y_test=train_test_split(X,y, test_size=20, shuffle=False)

lg=LinearRegression()
lg.fit(x_train,y_train)

y_pred=lg.predict(x_test)

print(lg.coef_)
print(mean_squared_error(y_test,y_pred))
print(r2_score(y_test,y_pred))

plt.scatter(x_test,y_test,color='black')
plt.plot(x_test,y_pred,color='blue')
plt.show()