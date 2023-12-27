def land_perimeter(arr):
    p = 0
    for i in arr:
        p+=i.count('X')
    p = p*4
    for i in arr:
        for j in i:
            if j =='X' and i[i.index(j)+1] == 'X':
                p-=1
    for i in arr:
        for j in i:
            if j == 'X' and arr[]
    return p

    #return 'Total land perimeter: {}'.format(p)

print(land_perimeter(["OXOOOX", "OXOXOO", "XXOOOX", "OXXXOO", "OOXOOX", "OXOOOO", "OOXOOX", "OOXOOO", "OXOOOO", "OXOOXX"]))
