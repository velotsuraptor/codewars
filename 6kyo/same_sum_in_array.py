def find_even_index(arr):
    for i in arr:
        if (sum(arr[:i])) == (sum(arr[i:])):
            return arr.index(i)
        else:
            continue
    else:
        return min(arr)
print(find_even_index([1,2,3,4,3,2,1]))