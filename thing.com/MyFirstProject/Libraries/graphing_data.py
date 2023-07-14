
import matplotlib.pyplot as plt
import numpy as np

def squared_values(x):
    return x * x

data = np.arange(100)

"""
for i in range(100):
    output = squared_values(i)
    data.append(output)
"""

print(data)

plt.plot(squared_values(data))
plt.show()