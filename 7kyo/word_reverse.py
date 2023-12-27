def reverse_words(text):
    ll = [i[::-1] for i in text.split(' ')]
    txt = ''
    for i in ll:
        txt +=i
    return txt