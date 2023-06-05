def Fibo(n):  # вернет фибоначи
    if n in [0, 1]:
        return n
    else:
        return Fibo(n - 1) + Fibo(n - 2)


def Prostoe(n1):
    if n1 > 3 and n1 % 2 != 0:
        if n1 % 3 != 0 and n1 % 5 != 0:
            return 'yes'
    else:
        return 'no'


def Recount(mynum):
    print(mynum, end='.')
    if mynum == 0:
        return mynum
    Recount(mynum - 1)


def power(base, exp):
    if exp == 1:
        return base
    if exp != 1:
        return base * power(base, exp - 1)

