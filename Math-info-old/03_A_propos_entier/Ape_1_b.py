def f(n):
    return 5 * n**3 + n

verif = True
for i in range(1 ,100000 + 1):
    if f(i) % 6 != 0:
        verif = False
        print("f(", i, ") = ", f(i), " n'est pas divisible par 7")
        break

print(verif)
# Divisible par 6