import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4,5,6,7,8,9,10])
y = np.array([10,25,15,30,20,35,28,40,32,45])
size = np.array([100,250,150,300,200,350,280,400,320,450])
colors = np.array([0,1,0,1,0,1,0,1,0,1])

plt.scatter(x, y, s=size, c=colors, alpha=0.7, cmap="viridis")
plt.title("Bubble Chart")
plt.colorbar(label="Color Variable")
plt.show()
