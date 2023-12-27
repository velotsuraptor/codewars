def digital_root(n):
    n = str(n)
    b = int()
    for i in n:
        b+=int(i)
    return b
print(digital_root(16))
