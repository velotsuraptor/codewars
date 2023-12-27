def dirReduc(arr):
    for i in arr:
        if i == 'NORTH':
            try:
                arr.remove('SOUTH')
                arr.remove('NORTH')
            except:
                continue
        if i == 'SOUTH':
            try:
                arr.remove('SOUTH')
                arr.remove('NORTH')
            except:
                continue
        if i == 'WEST':
            try:
                arr.remove('WEST')
                arr.remove('EAST')
            except:
                continue
        if i == 'EAST':
            try:
                arr.remove('EAST')
                arr.remove('WEST')
            except:
                continue
    return arr

print(dirReduc(["NORTH", "WEST", "SOUTH", "EAST", 'NORTH']))

