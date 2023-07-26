##Linear Regression
import numpy as np
import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9,10]
y = [10,12,13,15,16,17,18,19,20,21]

plt.scatter(x,y)
plt.show()

#SciPy is a scientific computation library that uses NumPy
import matplotlib.pyplot as plt
from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x,y)

def myPlot(x):
    return slope * x + intercept
myModel = list(map(myPlot, x))

plt.scatter(x,y)
plt.plot(x,myModel)
plt.show()
