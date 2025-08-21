import matplotlib.pyplot as plt
import numpy as np

data = np.array([[10,20,30],[15,25,35],[12,22,32],[18,28,38]])
avg = np.mean(data, axis=0)

plt.bar(['A','B','C'], avg)
plt.title("Bar Chart")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
