def sort_array(source_array):
    odds = [i for i in source_array if i%2]
    odds.sort()
    res = []
    conter = 0
    for i in source_array:
        if i%2:
            i = odds[0]
            odds.remove(odds[0])
            res.append(i)
        else:
            res.append(i)
    return res

print(sort_array([5, 3, 2, 8, 1, 4]))