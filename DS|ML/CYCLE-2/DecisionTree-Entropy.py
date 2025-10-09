from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier,plot_tree
import matplotlib.pyplot as plt

data=load_iris()
X,y=data.data,data.target

Xtrain,Xtest,ytrain,ytest=train_test_split(X,y,test_size=0.25,random_state=50)

classifier=DecisionTreeClassifier(criterion='entropy')
classifier.fit(Xtrain,ytrain)

print("-----Accuracy-------")
print("Train Accuracy : ",classifier.score(Xtrain,ytrain))
print("Test Accuracy : ",classifier.score(Xtest,ytest))


print("-----Figure-------")
plt.figure(figsize=(12,8))
plot_tree(classifier,filled=True,
         feature_names=data.feature_names,
         class_names=data.target_names.tolist())

plt.show()