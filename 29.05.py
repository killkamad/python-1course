def per():
    import random
    import itertools
    m = []
    for i in range(3):
        m.append(random.randint(-100, 100))

    n=list(itertools.permutations(m))
    for i in range(0,len(n)):
        print("Перестановки",n[i])
per()

print("="*30)

def arif_prog(a,d,n):
    l=[]
    l.append(a)
    for i in range(n):
        a +=d
        l.append(a)
    print("1) Арифметическая - ",l)
arif_prog(1,2,25)


def geom_prog(a, d, n):
    l = []
    l.append(a)
    for i in range(n):
        a *= d
        l.append(a)
    print("2) Геометрическая - ",l)
geom_prog(1, 2, 25)

def fibon_ch(n):
    a = 0
    b = 1
    l = []
    for i in range(n):
        a, b = b, a + b
        l.append(a)
    print("3) Фибоначи - ", l)
fibon_ch(25)

def even(n,a):
    l=[]
    c=0
    for i in range(n):
        if a%2==0:
            c = c + a
            l.append(c)
        else:
            c=c+2
            l.append(c)
    print("4) Четные числа - ",l)
even(25,8)

def stepen(n,step):
    l=[]
    c=0
    for i in range(n):
        c=i**step
        l.append(c)
    print("5) Возведение в степень - ",l)
stepen(25,2)

def martix(k):
    import random
    m=[]
    for i in range(k):
        n=[]
        for j in range(k):
            r=random.randint(0,1)
            n.append(r)
        m.append(n)
    for i in range(k):
        print()
        for j in range(k):
            print(m[i][j], end=' ')
martix(10)