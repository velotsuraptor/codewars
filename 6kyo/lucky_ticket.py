def luck_check(string):
    h1 = string[::2]
    h_1 = [int(i) for i in h1]
    h2 = string[3:]
    h_2 = [int(i) for i in h2]
    if sum(h_1)==sum(h_2):
        return True
    elif sum(h_1)!=sum(h_2):
        return False


print(luck_check('111111'))