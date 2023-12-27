dictionary_chars = {1:'A', 2:'B',3:'C', 4:'D', 5:'E', 6:'F', 7:'G', 8:'H', 9:'I', 10:'J', 11:'K', 12:'L', 13:'M',
         14:'N', 15:'O', 16:'P', 17:'Q', 18:'R', 19:'S', 20:'T', 21:'U', 22:'V', 23:'W', 24:'X', 25:'Y', 26:'Z'}

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                  'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                  'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def to_list(txt):
    for i in range(27):
        if f'{i}:' in txt:
            txt = txt.replace(f'{i}:','')
    if '1' or '2' in txt:
        txt = txt.replace('1','')
        txt = txt.replace('2','')
    return txt

def rot13(message):
    upper_alpabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                      'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lower_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                  'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    st = ''



    for i in message:
        if i in upper_alpabet:
            n = message.index(i)+6
            if n >= 26:
                n -= 26
                st+=upper_alpabet[n]
            else:
                st+=upper_alpabet[n]
        if i in lower_alphabet:
            n = message.index(i)+6
            if n >= 26:
                n -= 26
                st+=lower_alphabet[n]
            else:
                st+=lower_alphabet[n]
        else:
            st += i
    return st




def trial(func, result):
    if func == result:
        print('passed')
    else:
        print('try again must be \'\'',result, '\'\' not \'\'', func, '\'\'')

trial(rot13('test'),'grfg')
trial(rot13('aA bB zZ 1234 *!?%'), 'nN oO mM 1234 *!?%')
