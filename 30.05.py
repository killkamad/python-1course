import random
def monte(p,mounth,rangee):
    m=[]
    w=0
    l=0
    for i in range(mounth):
        n=[]
        for j in range(rangee):
            r = round(random.uniform(0, 1),2)
            if r<=p:
                n.append(1)
            elif r>p:
                n.append(0)
        m.append(n)
    for i in range(mounth):
        print()
        for j in range(rangee):
            print(m[i][j], end=' ')
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j]==1:
                w+=1
            else:
                l+=1
    print()
    print('win - ',w)
    print('lose - ',l)

#monte(0.5,12,25)

def proj2(work,rab):
    m=[]
    l=[]
    rabl=[]
    workl=[]
    for i in range(1,rab+1):
        rabl.append(i)
    print(rabl)

    for i in range(1,work+1):
        workl.append(i)
    print(workl)
#####################################
    for i in range(work):
        n=[]
        # r = random.randint(0, len(rabl)-9)
        # workl.pop()
        for j in range(rab):
            n.append(0)
        m.append(n)

    for i in range(work):
        print()
        for j in range(rab):
            print(m[i][j], end=' ')

    for i in range(len(m)):
        for j in range(len(m[i])):
            r = random.randint(0, len(rabl))


#proj2(9,12)