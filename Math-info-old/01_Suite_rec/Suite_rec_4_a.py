import matplotlib.pyplot as plt

# 4.a

u=[1, 2]

def a4 (terme1, terme2):
    return terme2 - 3*terme1

for i in range(240):
    u.append(a4(u[-2], u[-1]))

terme=range(len(u))

plt.plot(terme, u)
plt.xlabel("terme")
plt.ylabel("valeur")
plt.grid()
plt.show()

# La suite diverge
