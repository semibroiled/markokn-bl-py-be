import random

def lotto(x, y=6, a=1, b=2, c=3, d=4, e=5, f=6, g=7):
    lst1 = []
    for i in range(x):
        for i in range(y):
            lst1.append(random.randint(1,49))
    superzahl = random.choice([a,b,c,d,e,f,g])
    return lst1, superzahl

print(lotto(6))



