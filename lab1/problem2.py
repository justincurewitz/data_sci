import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
n = 1000
p = 0.5
z = np.random.binomial(n, p, 1000)
z = z.astype(float)
for i in range(0, 10):
  z[i] = z[i]*.001
print z
plt.hist(z)
plt.title("Problem 2")
plt.show()
