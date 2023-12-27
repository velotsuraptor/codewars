def solution(s):
    lis = [i for i in s]
    for i in lis:
        if i.isupper():
            lis[lis.index(i)] = ' '+i
    st = ''
    for i in lis:
        st+=i
    return st

print(solution("helloWorld"))

