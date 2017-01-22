import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
n = 1000
p = 0.5
ans = np.random.binomial(n, p, 1000)
print ans
plt.hist(ans)
plt.show()
