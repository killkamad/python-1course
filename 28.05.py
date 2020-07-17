def bank():
    chose=int(input('Введите 1 или 2: '))
    if chose==1:
        i=int(input('Процентная ставка - '))
        p=int(input('Взнос - '))
        n=int(input('Срок - '))

        s=p*(1+i)**n
        print(s)
    if chose==2:
        i=int(input('Процентная ставка - '))
        s=int(input('Взнос - '))
        n=int(input('Срок - '))

        p=s/((1+i)**n)
        print(round(p,2))

while True:  #Бесконечный цикл пока пользователь не выберет вариант - нет
    restart=input('Введите да, чтобы продолжить или нет, чтобы закончить - ')
    if restart=='да':
        bank()
    else:
        break