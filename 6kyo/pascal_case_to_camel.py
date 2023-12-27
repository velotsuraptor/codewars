def paasc(text):
    for i in text:
        if i.isupper():
            i.lower()
            text = text.replace(i, '_'+i)
    for i in text:
        if i.isupper():
            i = i.lower()
    return text

print(paasc('PascalIsWorseThanPython'))