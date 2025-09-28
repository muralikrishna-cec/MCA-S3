# -------------------- Method 1: Using return_X_y --------------------

# Import required libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

# Load dataset directly as (features, labels)
x, y = load_iris(return_X_y=True)   # return_X_y=True gives only data & target, no metadata

# Split dataset into training (50%) and testing (50%)
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.5, random_state=1)

# Initialize Naive Bayes classifier
gnb = GaussianNB()

# Train the model and predict test labels
ypred = gnb.fit(xtrain, ytrain).predict(xtest)

# Print accuracy (score = correct predictions / total predictions)
print("Naive Bayes Score:", gnb.score(xtest, ytest))

# Predict for a new flower
xnew = [[5, 5, 4, 4]]
ynew = gnb.predict(xnew)
print("Predicted output for [5,5,4,4]:", ynew)   # Gives class index (0,1,2)




print("\n-------------------- Another Method --------------------\n")


# -------------------- Method 2: Using metadata --------------------

# Import required libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

# Load dataset with metadata
iris = load_iris()
X, y = iris.data, iris.target          # features and labels
target_names = iris.target_names       # class names (setosa, versicolor, virginica)

# Split dataset into training (50%) and testing (50%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=1)

# Initialize and train Naive Bayes model
gnb = GaussianNB()
gnb.fit(X_train, y_train)

# Print accuracy
print("Naive Bayes Score:", gnb.score(X_test, y_test))

# Predict for a new flower
xnew = [[5, 5, 4, 4]]
ynew = gnb.predict(xnew)
print("Predicted output for [5,5,4,4]:", target_names[ynew][0])  # Converts index → class name

