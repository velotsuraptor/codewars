def is_valid_walk(walk):
    l = {i: walk.count(i) for i in walk}
    nl = []
    for i in l:
        nl.append(l.get(i))
    if sum(nl)!=10:
        return False
    if nl[0]!=nl[1]:
        return False
    else:
        return True

print(is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e']))