import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
ar = np.random.normal(0, 5, 25000)
total = 0
for x in range(0, 25000):
  total = total + ar[x]
mean = total/25000
stand = 0
for x in range(0, 25000):
  stand = stand + np.square(ar[x] - mean)
stand = stand/25000
stand = np.sqrt(stand)
print "mean:"
print mean
print "standard deviation: "
print stand
