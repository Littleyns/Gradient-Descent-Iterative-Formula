import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import derivative
import math
f = lambda x : (x**2)**(1/2)
X = np.linspace(-100,100,100)
plt.plot(X,f(X))
a0=-100
alpha=0.1
plt.scatter(a0,f(a0),c='r')
for i in range(1000):
    a0=a0-(alpha*derivative(f,a0))
    plt.scatter(a0,f(a0),c='r')
plt.show()