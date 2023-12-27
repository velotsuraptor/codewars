def digital_root(n):
    n = str(n)
    b = int()
    for i in n:
        b+=int(i)
    if b<10:
        return b
    else:
        return digital_root(b)