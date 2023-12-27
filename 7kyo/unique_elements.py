def find_uniq(arr):
    unique = [i for i in arr if arr.count(i) == 1]
    return unique[0]


print(find_uniq([1, 1, 1, 2, 1, 1]))

# 519
# 681
