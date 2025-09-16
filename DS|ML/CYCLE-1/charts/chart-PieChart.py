import matplotlib.pyplot as plt
import numpy as np

data = np.array([[10,20,30],[15,25,35],[12,22,32],[18,28,38]])
cols_sums = np.sum(data, axis=0)

labels = ["Col 1","Col 2","Col 3"]
plt.pie(cols_sums, labels=labels, autopct="%1.1f%%", startangle=140)
plt.title("Pie Chart")
plt.show()
