def trial(func, result):
    if func == result:
        return print('passed')
    else:
        return print(f'try again must be \'{result}\' not \'{func}\'')

def dirReduc(arr):
    result = []
    for i in arr:
        try:
            if i == 'NORTH' and arr[arr.index(i)+1] == 'SOUTH':
                arr.remove(arr.index(i))
                arr.remove(arr.index(i.next))
        except:
            return arr
    return arr

trial(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]), ['WEST'])