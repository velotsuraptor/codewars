def increment_string(strng):
    try:
        a1 = int(strng[-1])
        return strng.replace(strng[-1], str(a1+1))
    except:
        return strng+'1'

print(increment_string("foo"))
print(increment_string("foo1"))
