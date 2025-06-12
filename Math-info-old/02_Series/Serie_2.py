def f(a):
    s=2
    for n in range(1, 100):
        s*=(1+a**n)
    return s
liste=[]
for i in range(100):
    liste.append(-5+i/10)
val=[]
print(liste)

for i in liste:
    val.append(f(i))

import matplotlib.pyplot as plt
plt.plot(liste, val)
plt.show()