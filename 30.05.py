def monte(p,mounth,rangee):
    import random
    m=[]
    w=0
    l=0
    for i in range(mounth):
        n=[]
        for j in range(rangee):
            #Создание случайного числа от (0 до 1)
            #и округления его до 2 знаков после запятой
            r = round(random.uniform(0, 1),2)
            #Проверка: если число r меньше или равно
            #фиксированному числу p, то в матрицу добовляется
            #число 1, если r больше p, то добовляется 0
            if r<=p:
                n.append(1)
            elif r>p:
                n.append(0)
        m.append(n)
    for i in range(mounth):   #Этот for предает вид матрицы
        print()
        for j in range(rangee):
            print(m[i][j], end=' ')
    for i in range(len(m)):   #Этот for читает всю матрицу
        for j in range(len(m[i])):  #и считывает все нули и единицы
            if m[i][j]==1:
                w+=1
            else:
                l+=1
    print()
    print('win - ',w)
    print('lose - ',l)
monte(0.5,12,25)

def proj2(work,rab):
    import random
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
##################################################
import random
def bag(W, wt, val, n):
    #Главный кейс
    if n == 0 or W == 0 :
        return 0
    #Если вес n-ого предмета больше вместимости ранца
    #То этот предмет не может быть включен в решение
    if (wt[n-1] > W):
        return bag(W, wt, val, n-1)
    #Возвращает максимумальную возможную сумму
    #без повторения элементов
    else:
        S =  max(val[n-1] + bag(W-wt[n-1], wt, val, n-1),
                   bag(W, wt, val, n-1))
        return (S)
val = []  #Стоимость
wt = []   #Вес
W = 15    #Ограниченный вес
#Создание случайных значений для цены от (1,10)
for i in range(0, 5):
    rval = random.randint(1, 10)
    val.append(rval)
print('Цена в $ - ', val)
#Создание случайных значений для веса от (1,12)
for i in range(0, 5):
    rwt = random.randint(1, 12)
    wt.append(rwt)
print('Вес в кг - ', wt)
n = len(val)
print(bag(W, wt, val, n))