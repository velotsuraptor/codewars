def trial(func, result):
    if func == result:
        return print('passed')
    else:
        return print(f'try again must be \'{result}\' not \'{func}\'')


def calculation(numm):
    if numm <9:
        return numm
    #print(numm)
    lll = [int(i) for i in str(numm)]
    base = 1
    for i in lll:
        #print(base)
        base *=i
        #print(base)
    numm = base
    return calculation(numm)

def persistence(n):
    if n<9:
        return 0
    else:
        return calculation(n)



trial(persistence(39), 3)
trial(persistence(4), 0)
trial(persistence(25), 2)
trial(persistence(999), 4)
