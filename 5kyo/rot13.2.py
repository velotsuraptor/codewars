

def rot13(message):
    entry = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    fin = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'

    st = ''
    for i in message:
        if i in entry:
            st+=fin[entry.index(i)]
        else:
            st+=i
    return st