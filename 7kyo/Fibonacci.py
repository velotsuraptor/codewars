def fibonacci(n, num):
    if n < 2:
        print(num)
    elif len(num) < n:
        if len(num) != n:
            num.append(num[-1] + num[-2])
            fibonacci(n, num)
    if len(num) == n:
        return num


print(fibonacci(25, [0, 1]))
