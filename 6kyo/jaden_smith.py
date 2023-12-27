def to_jaden_case(string):
    s = string.split()
    st = ''
    for i in s:
        j = i[0].upper()
        i.replace(i,j)
        st+=i+' '
    return st

print(to_jaden_case('mamma mia'))