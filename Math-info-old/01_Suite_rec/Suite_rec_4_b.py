u=[-1, -2]

def suite (un, deux, n):
    return (1/5)*(un + 4*deux + 2**n)

for i in range(80):
    u.append(
        suite(u[-2], u[-2], len(u)-2)
    )


terme=range(len(u))


import matplotlib.pyplot as plt
plt.plot(terme, u)
plt.show()