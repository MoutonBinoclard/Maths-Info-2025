def x(t):
    return (t-1)/(t**2-4)

def y(t):
    return (t**2-3)/(t+2)

X=[]
Y=[]

deb=1
fin=25
pas=0.0001

while deb<fin:
    X.append(x(deb))
    Y.append(y(deb))
    deb+=pas


import matplotlib.pyplot as plt
plt.plot(X, Y)
plt.show()