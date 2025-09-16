import matplotlib.pyplot as plt
import numpy as np

data = np.array([[10,20,30],[15,25,35],[12,22,32],[18,28,38]])
x = data[:,0]
y = data[:,1]

plt.scatter(x, y, c='blue', marker='o')
plt.title("Scatter Plot")
plt.show()
