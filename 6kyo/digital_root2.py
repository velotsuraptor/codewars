def digital_root(n):
    if n > 10:
        while n>10:
            k = [int(i) for i in str(n)]
            n = sum(k)
            if n<10:
                return n
    if n<10:
        return n
    else:
        return 1


print(digital_root(1651986284840011))