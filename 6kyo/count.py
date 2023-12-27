char = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
def count(string):
    dic = dict()
    for i in string:
        if i in dic:
            continue
        if i not in dic:
            if i.upper() in char:
                n = string.count(i)
                dic.update({i:n})
    return dic

print(count('aba'))