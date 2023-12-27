def tribonacci(signature, n):
    res = []
    if n<=3:
        for i in range(n):
            res.append(signature[i])
        return res
    if n>3:
        res = signature
        while len(res)!=n:
            res.append(res[-3]+res[-2]+res[-1])
        return res

print(tribonacci([1, 1, 1], 10))