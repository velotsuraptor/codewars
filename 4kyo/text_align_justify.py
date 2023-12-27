def justify(text, width):
    lst1 = []
    for i in text:
        if i%width:
            text = text.replace(i, i+'\n')

    return text

with open('text.txt', 'r') as t:
    txt = t.read()
    justify(txt, 20)
