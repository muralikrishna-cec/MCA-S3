from sklearn import datasets
from sklearn import svm
from sklearn import metrics
from sklearn.model_selection import train_test_split

data=datasets.load_breast_cancer()

x_train,x_test,y_train,y_test=train_test_split(data.data,data.target,test_size=0.25,random_state=50)

cls=svm.SVC(kernel='linear')
cls.fit(x_train,y_train)
y_pred=cls.predict(x_test)
print("val",y_test)
print("pred",y_pred)

print(metrics.accuracy_score(y_test,y_pred))
print(metrics.precision_score(y_test,y_pred))
print(metrics.recall_score(y_test,y_pred))
