def last_digit(lst):
    num = int()
    for i in lst:
        ind = lst.index(i)
        while ind > len(lst):
            num = lst[ind]**lst[ind+1]
    return str(num)[-1]

last_digit([2, 2, 2, 0])