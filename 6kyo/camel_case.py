def to_camel_case(text):
    ttt = ''
    n = text.replace('-',' ')
    n = n.replace('_', ' ')
    a = n.split()
    for i in a:
        ttt+=i.capitalize()
    if ttt[0].islower():
        k = ttt.replace(ttt[0],ttt[0].lower())
        return k
    else:
        return ttt

print(to_camel_case("the_stealth_warrior"))