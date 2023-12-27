def fibonacci(n):
    num = [0, 1]
    if n <= 2:
        for i in num[:n]:
            yield i
    elif len(num) < n:
            num.append(num[-1] + num[-2])
            fibonacci(n)
    elif len(num) == n:
        for i in num:
            yield i

#print(fibonacci(25))

for i in fibonacci(25):
    print(i)