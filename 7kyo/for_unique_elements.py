def find_uniq(arr):
    unique = None
    for i in arr:
        n = arr.count(i)
        if n == 1:
            unique = i
    return unique

# 504