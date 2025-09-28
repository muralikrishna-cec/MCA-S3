# Import libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

# Load dataset
iris = load_iris()
x = iris.data
y = iris.target

# Split dataset (70% training, 30% testing)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1)

# Initialize KNN classifier with k=3
c_knn = KNeighborsClassifier(n_neighbors=3)

# Train the model
c_knn.fit(x_train, y_train)

# Predict on test data
y_pred = c_knn.predict(x_test)

# Print accuracy
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))

# Test with a new sample
sample = [[2, 2, 2, 2]]
pred = c_knn.predict(sample)

# Convert numerical prediction into class name
pred_v = [iris.target_names[p] for p in pred]
print(pred_v)
