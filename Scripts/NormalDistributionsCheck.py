import numpy as np
import matplotlib.pyplot as plt

s1, s2 = 1, 2
n = 10000
x1 = np.random.normal(0, s1, n)
x2 = np.random.normal(0, s2, n)
y = x1 + x2



plt.hist(y, bins=100)
plt.hist(x2, bins=100)

plt.hist(x1, bins=100)
plt.legend(["x1", "x2","y"])
plt.show()