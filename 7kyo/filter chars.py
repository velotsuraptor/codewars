def filter_list(l):
    return [i for i in l if type(i) == str]

print(filter_list([1, 2, 'a', 'b']))
