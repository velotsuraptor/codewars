def is_pangram(s):
    alph = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    s = s.replace(',','')
    s = s.replace('.','')
    s = s.replace(' ','')
    s = s.replace('!','')
    nst = ''
    for i in s:
        nst+=i.upper()
    srt = sorted(nst)
    srt = list(dict.fromkeys(srt))
    if alph == srt:
        return True
    else:
        return False

print(is_pangram("The quick, brwn fx jumps ver the lazy dg!"))