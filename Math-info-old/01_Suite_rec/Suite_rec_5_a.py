# Que peut-on dire à propos de la convergence des ces deux suites ?
# Je sais pas


av1=[1]
bv1=[3]

av2=[148]
bv2=[30.1]


def avancement(suite1, suite2):
    new1 = (suite1[-1] + 2*suite2[-1])/3
    new2 = (suite1[-1]*(suite2[-1]**2))**(1/3)
    suite1.append(new1)
    suite2.append(new2)
    return suite1, suite2

for i in range(50):
    av1,bv1=avancement(av1,bv1)
    av2,bv2=avancement(av2,bv2)


import matplotlib.pyplot as plt

plt.plot(range(len(av1)), av1, '-o', label='Suite av1')
plt.plot(range(len(bv1)), bv1, '-o', label='Suite bv1')
plt.plot(range(len(av2)), av2, '-o', label='Suite av2')
plt.plot(range(len(bv2)), bv2, '-o', label='Suite bv2')

plt.legend()
plt.show()