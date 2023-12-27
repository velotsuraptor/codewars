from math import sqrt
def comp(array1, array2):
    for i in array1:
        for j in array2:
            if sqrt(i)*sqrt(i) == j:
                return True
            else:
                return False


a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
print(comp(a1, a2))