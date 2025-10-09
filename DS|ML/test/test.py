from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

iris=load_iris()
x=iris.data
y=iris.target

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=1)
c_knn=KNeighborsClassifier(n_neighbors=1)
c_knn.fit(x_train,y_train)
y_pred=c_knn.predict(x_test)
print("Accuracy",metrics.accuracy_score(y_test,y_pred))
sample=[[4,4,4,4]]
pred=c_knn.predict(sample)
pred_v=[iris.target_names[p] for p in pred]
print(pred_v)      


from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

x,y =load_iris(return_X_y=True)

xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.5,random_state=1)
gnb=GaussianNB()
ypred=gnb.fit(xtrain,ytrain).predict(xtest)

#print(ypred)

print("naive bayes score :",gnb.score(xtest,ytest))
xnew=[[3,1,1,1]]
ynew=gnb.predict(xnew)
print("predicted op  : ",ynew)
pred_v=[iris.target_names[p] for p in ynew]
print(pred_v)   


import pandas as pd
import numpy as np

Symptoms={
    'Chills':['Y','Y','Y','N','N','N','N','Y'],
    'running nose':['N','Y','N','Y','N','Y','Y','Y'],
    'headache':['mild','no','strong','mild','no','strong','strong','mild'],
    'fever':['Y','N','Y','Y','N','Y','N','Y'] ,
    'hasFlue':['N','Y','Y','Y','N','Y','N','Y']
}

db=pd.DataFrame(Symptoms)
db      


from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
import pandas as pd
from sklearn.preprocessing import LabelEncoder

Symptoms={
    'Chills':['Y','Y','Y','N','N','N','N','Y'],
    'running nose':['N','Y','N','Y','N','Y','Y','Y'],
    'headache':['mild','no','strong','mild','no','strong','strong','mild'],
    'fever':['Y','N','Y','Y','N','Y','N','Y'] ,
    'hasFlue':['N','Y','Y','Y','N','Y','N','Y']
}

df=pd.DataFrame(Symptoms)
df_encoded=df.apply(LabelEncoder().fit_transform)

X=df_encoded.drop('hasFlue',axis=1)
y=df_encoded['hasFlue']

gnb=GaussianNB()
y_pred=gnb.fit(X,y).predict(X)

print("predicted label",y_pred)
print("Naive bayes score",gnb.score(X,y))

xnew=pd.DataFrame([[1,0,1,1]],columns=X.columns)

ynew=gnb.predict(xnew)
print('prediction',ynew)    

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
import pandas as pd
from sklearn.preprocessing import LabelEncoder

Symptoms={
    'Chills':['Y','Y','Y','N','N','N','N','Y'],
    'running nose':['N','Y','N','Y','N','Y','Y','Y'],
    'headache':['mild','no','strong','mild','no','strong','strong','mild'],
    'fever':['Y','N','Y','Y','N','Y','N','Y'] ,
    'hasFlu':['N','Y','Y','Y','N','Y','N','Y']
}

df=pd.DataFrame(Symptoms)

encoders={}
df_encoded=pd.DataFrame()


for col in df.columns:
    le=LabelEncoder()
    df_encoded[col]=le.fit_transform(df[col])
    encoders[col]=le
    
X=df_encoded.drop('hasFlu',axis=1)
y=df_encoded['hasFlu']


gnb=GaussianNB()
gnb.fit(X,y)

print("Naive Bayes score :",gnb.score(X,y))

xnew=pd.DataFrame([['Y','N','mild','Y']],columns=X.columns)

for col in xnew.columns:
    xnew[col]=encoders[col].transform(xnew[col])
    
ynew=gnb.predict(xnew)

print("predicted op ",encoders['hasFlu'].inverse_transform(ynew)[0])

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

iris=load_iris()
X=iris.data
y=iris.target
target_names=iris.target_names

xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2,random_state=1)

gnb=GaussianNB()
ypred=gnb.fit(xtrain,ytrain).predict(xtest)

#print("Predicted labels",target_names[ypred])


xnew=[[5,5,4,4]]
ynew=gnb.predict(xnew)

print("predicted op [5,5,4,4] : ",target_names[ynew][0])
print("naive bayes score :",gnb.score(xtest,ytest))