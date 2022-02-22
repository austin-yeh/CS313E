import math
import numpy as np
import matplotlib.pyplot as plt

msize = 5

n = np.arange(0, msize, 0.1)

# red dashes, blue squares and green triangles
# plt.plot(t, t, 'r--', t, t**3.5 - 2**10, 'bs', t, 100*t**2.1 + 50, 'g^')

plt.plot(n, (2**10)*n + (2**10) , 'red', n, n**3.5 - 1000, 'blue', n, 100*n**2.1 + 50, 'green')

plt.xlim(0, msize)
plt.rcParams["figure.figsize"] = (7,7)
plt.show()