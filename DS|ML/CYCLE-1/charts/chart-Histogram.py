import matplotlib.pyplot as plt
import numpy as np

data = np.array([[10,20,30],[15,25,35],[12,22,32],[18,28,38]])
all_values = data.flatten()

plt.hist(all_values, bins=5, color="skyblue", edgecolor="black")
plt.title("Histogram")
plt.show()
