def trial(func, result):
    if func == result:
        return print('passed')
    else:
        return print(f'try again must be \'{result}\' not \'{func}\'')


def calculation(n):
    counter = 0
    while n > 9:
        counter+=1
        lll = [int(i) for i in str(n)]
        base = 1
        for i in lll:
            base *= i
        n = base
    if n<=9:
        return counter

def persistence(n):
    if n<9:
        return 0
    else:
        return calculation(n)

trial(persistence(39), 3)
trial(persistence(4), 0)
trial(persistence(25), 2)
trial(persistence(999), 4)
