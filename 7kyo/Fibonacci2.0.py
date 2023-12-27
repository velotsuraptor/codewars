def fibonacci(n):
    num = [0, 1]
    if n <= 2:
        for i in num[:n]:
            yield i
    if n >2:
        while n > len(num):
            num.append(num[-1] + num[-2])
        for i in num:
            yield i

#print(fibonacci(25))

for i in fibonacci(25):
    print(i)