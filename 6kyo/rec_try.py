def rec(ln, num):
    if len(num) == ln:
        return int(num)
    return rec(ln, num + str(int(num[-1]) + int(num[-2])))


#print(rec(11, '011'))

