u=[1, 0, 0]
# u0, u1, u2


def suite(u):
    num_terme = len(u)-3
    newu = (u[-1]*(num_terme + 2) + u[-3])/(num_terme + 3)
    u.append(newu)
    return u

for i in range(50):
    u = suite(u)

import matplotlib.pyplot as plt

plt.plot(range(len(u)), u)
plt.show()