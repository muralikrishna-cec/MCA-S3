import matplotlib.pyplot as plt
import numpy as np

A = np.array([[1,2,3,4],[1,4,9,16]])
plt.plot(A[0], A[1], color='red', linestyle='--', marker='o')
plt.title("Test")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend(["Data"])
plt.grid(True)
plt.show()
