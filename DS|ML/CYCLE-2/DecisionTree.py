import pandas as pd
import numpy as np

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier 
from sklearn.metrics import accuracy_score

from sklearn.tree import export_graphviz
from IPython.display import Image 
import pydotplus





iris_data=load_iris()

X=iris_data.data
y=iris_data.target





print("------------Dataset info------------")

print(f"shape of data :{X.shape}")
print(iris_data.data.shape)

#display(X.shape,y.shape)

print(f"shape to predict : {iris_data.target_names}")
print(f"Features : {iris_data.feature_names}\n")

xtrain, xtest, ytrain, ytest=train_test_split(X,y,random_state=50,test_size=0.25)





print("----------Training with gini----------")

classifier_gini=DecisionTreeClassifier()
classifier_gini.fit(xtrain,ytrain)
ypred_gini=classifier_gini.predict(xtest)

print(f"Accuracy on train data (gini): {accuracy_score(y_true=ytrain,y_pred=classifier_gini.predict(xtrain))}")
print(f"Accuracy on test data (gini): {accuracy_score(y_true=ytest,y_pred=ypred_gini)}\n")





print("----------Training with Entropy----------")

classifier_entropy=DecisionTreeClassifier(criterion='entropy')
classifier_entropy.fit(xtrain,ytrain)
ypred_entropy=classifier_entropy.predict(xtest)

print(f"Accuracy on train data (entropy): {accuracy_score(y_true=ytrain,y_pred=classifier_entropy.predict(xtrain))}")
print(f"Accuracy on test data (entropy): {accuracy_score(y_true=ytest,y_pred=ypred_entropy)}\n")





print("----------Training with Entropy 50 sample----------")

classifier_entropy50=DecisionTreeClassifier(criterion='entropy',min_samples_split=50)
classifier_entropy50.fit(xtrain,ytrain)
ypred_entropy50=classifier_entropy.predict(xtest)

print(f"Accuracy on train data  (entropy 50): {accuracy_score(y_true=ytrain,y_pred=classifier_entropy50.predict(xtrain))}")
print(f"Accuracy on test data (entropy 50): {accuracy_score(y_true=ytest,y_pred=ypred_entropy50)}\n")





print("----------Visualization----------")

dot_data=export_graphviz(classifier_gini,
                         out_file=None,
                         feature_names=iris_data.feature_names,
                         class_names=iris_data.target_names,
                         filled=True,
                         rounded=True,
                         special_characters=True)

graph=pydotplus.graph_from_dot_data(dot_data)
graph.write_png('iris_decision_tree.png')
print("visualization saved")

Image(graph.create_png())