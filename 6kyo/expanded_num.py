def expanded_form(num):
    list = [i for i in str(num)]
    nn = len(list)-1
    for i in list:
        el = i+'0'*nn
        list.insert(list.index(i),el)
        list.remove(i)
        nn-=1
    st = ''
    for i in list:
        if i[0]== '0':
            continue
        else:
            st+=i +' + '
    return st[:-3]



print(expanded_form(70304))
