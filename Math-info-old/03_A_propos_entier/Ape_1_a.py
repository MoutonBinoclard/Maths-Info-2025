def f(n):
    return n * (n**6 -1)

verif = True
for i in range(1 ,100000 + 1):
    if f(i) % 7 != 0:
        verif = False
        print("f(", i, ") = ", f(i), " n'est pas divisible par 7")
        break

print(verif)
# Divisible par 7