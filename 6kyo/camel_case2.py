x = ' f f f f f f fgf f fg fhf'
'''def to_camel_case(text):
    ttt = ''
    if '-' in text:
        a = text.split('-')
    if '_' in text:
        a = text.split('_')
    if ' ' in text:
        a = text.split()
    for i in a:
        for j in i:
            if i.
    for i in a:
        ttt+=i
    return ttt

print(to_camel_case('A-B-c'))'''

y = 'word'
#print(y.capitalize())

def to_camel_case(text):
    ttt = ''
    for i in text:
        if i == '_':
            i = ' '
        if i == '-':
            i = ' '
    a = text.split()
    for i in a:
        ttt += i.capitalize()
    return ttt

print(to_camel_case('A_b a'))