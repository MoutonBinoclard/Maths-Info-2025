import math as mt

u=[0, 1]

def suite(un, deux):
    return mt.sqrt(un) + mt.sqrt(deux)

for i in range(80):
    u.append(
        suite(u[-2], u[-1])
    )

terme=range(len(u))
import matplotlib.pyplot as plt
plt.plot(terme, u)
plt.show()

# Suite converge vers 4