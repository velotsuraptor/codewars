def array_diff(a, b):
    s = []
    for i in a:
        if i not in b:
            s.append(i)
    return s

# 495