def accum(s):
    st1 = ''
    s.split()
    for i in s:
        st1 += i.upper()+str(i.lower()*s.index(i))+'-'
    return st1[0:-1]

print(accum('ABABA'))