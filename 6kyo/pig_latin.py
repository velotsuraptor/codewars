def pig_it(text):
    txt = text.split(' ')
    ntxt = ''
    for i in txt:
        i1 = i[0]
        i = i.replace(i1,'')
        i+= i1+'ay'+' '
        ntxt+=i
    return ntxt[:-1]
print(pig_it('This is my string'))
