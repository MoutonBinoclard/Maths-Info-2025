def somme(n):
    s=0
    for k in range(1, n+1):
        s+=1/(k ** (0.5))
    
    return s

n0=1
while somme(n0)<=10:
    n0+=1

print(n0)
print(somme(n0))

# n=33