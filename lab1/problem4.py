import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
mean = [-5, 5]
cov = [[20, .8], [.8, 30]]
x = np.random.multivariate_normal(mean, cov, 10000)
x1 = 0
x2 = 0
for y in range(0, 10000):
  x1 = x[y][0] + x1
  x2 = x[y][1] + x2
x1 = x1/10000
x2 = x2/10000
sig1 = 0
sig2 = 0
s1s2 = 0
for i in range(0, 10000):
  sig1 = sig1 + np.square(x1 - x[i][0])
  sig2 = sig2 + np.square(x2 - x[i][1])
  s1s2 = s1s2 + ((x1 - x[i][0])*(x2 - x[i][1]))
sig1 = sig1/10000
sig2 = sig2/10000
s1s2 = s1s2/10000
print "x1: ", x1
print "x2: ", x2
covariance = [[sig1, s1s2],[s1s2, sig2]]
print covariance
