def unique_in_order(iterable):
    un = [i for i in iterable]
    u = list()
    prev = None
    for i in un:
        try:
            if i!=prev:
                u.append(i)
        except:
            u.append(i)
    return u

print(unique_in_order('AAAABBBCCDAABBB'))