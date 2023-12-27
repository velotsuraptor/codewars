arr = [2, 3, 1, 9, 4, 5, 6, 10, 7]

m = max(arr)
arr.sort()
print(arr)
arr2 = list()
for i in range(m):
    if i not in arr:
        arr2.append(i)
arr
print(arr2)