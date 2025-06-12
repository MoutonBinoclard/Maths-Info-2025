import math as mt

def somme(n):
    s=0
    for k in range(2, n+1):
        s+=1/(k*mt.log(k))
    return s

n0=1
while somme(n0)<=3:
    n0+=1

print(n0)
print(somme(n0))

# n1 = 8718

