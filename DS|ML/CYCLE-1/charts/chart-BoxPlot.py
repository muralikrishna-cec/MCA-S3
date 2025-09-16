import matplotlib.pyplot as plt
import numpy as np

data = np.array([[10,20,30],[15,25,35],[12,22,32],[18,28,38]])
plt.boxplot(data, labels=['A','B','C'])
plt.title("Box Plot")
plt.show()
