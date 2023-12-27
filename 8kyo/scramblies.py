def scramble(s1, s2):
    ss1 = [i for i in s1]
    ss2 = [i for i in s2]
    if ss1 in ss2:
        return True
    else:
        return False


print()