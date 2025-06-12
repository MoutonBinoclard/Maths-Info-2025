import numpy as np

def simpson(f, a, b, n):
    s = 0
    s1 = 0
    for k in range(1, n):
        s += f(a + (b - a) * k / n)
    for k in range(n):
        s1 += f(a + (k + .5) * (b - a) / n)
    return (b - a) / (6.0 * n) * (f(a) + f(b) + 2 * s + 4 * s1)


def f1(x):
    if x == 0:
        return 1.0
    return np.sin(x) / x


def f2(x):
    return np.e ** (-x ** 2)


def f3(x):
    if x == 0:
        return 0
    return 1/(2*(-np.log(x))**.5)

def f(x):
    return np.sin(x**2)

print(simpson(f, 0.0, 1.0, 100))

print(simpson(f1, 0.0, 1.0, 100))

print(simpson(f2, 0.0, 1.0, 100))
print(simpson(f2, 0.0, 1000, 10000), (np.pi**.5)/2)