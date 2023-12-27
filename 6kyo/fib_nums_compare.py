def fib(num):
    lst = [0,1,1]
    while lst[-1]*lst[-2]<num:
        lst.append(lst[-1]+lst[-2])
    if lst[-1]*lst[-2]>= num:
        if lst[-1]*lst[-2] == num:
            return True
        if lst[-1] * lst[-2] > num:
            return False
print(fib(4895))