def remove_every_other(my_list):
    k = len(my_list)
    nl = list()
    for i in range(0,k,2):
        for j in my_list:
            if my_list.index(j)==i:
                nl.append(j)
    return nl

print(remove_every_other([1,2,1,2,1,2,1,2,1,2,1,2,1,2]))