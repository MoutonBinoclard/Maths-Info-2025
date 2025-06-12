# 3

# 3.a

# La suite est-elle definie ?
# NON, U0= 3.9999999
# U1 =~ 39000
# U2 negatif -> pas def


# On change I
# I = ]0, 1[

import scipy as sp
from scipy.optimize import bisect
import math as mt
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return 1/(2-mt.sqrt(x))


def suite(u,n):
    a=[u] #abs
    o=[0] #ord
    for i in range(n):
        o.append(f(a[-1]))
        a.append(a[-1])
        o.append(f(a[-1]))
        a.append(f(a[-1]))
    return a,o


a,o=suite(2.6,10)
c=np.linspace(0,3.99,20)
d=[f(i) for i in c]
plt.xlim(0,3.99)
plt.ylim(0,3.99)
plt.plot(c,d)
plt.plot(c,c)
plt.plot(a,o)
plt.show()