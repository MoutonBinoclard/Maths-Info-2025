def f (couple_xy):
    x, y = couple_xy
    return (y, 111 - 1130/y + 3000/(x*y))

u=[(108, 115)]

for i in range(30):
    u.append(f(u[-1]))

import matplotlib.pyplot as plt

plt.plot(range(len(u)), [u[i][0] for i in range(len(u))], '-x', label='x')
plt.plot(range(len(u)), [u[i][1] for i in range(len(u))], '-x', label='y')
plt.legend()
plt.show()