def generate_hashtag(s):
    s = s.split(' ')
    l1 = [i.capitalize() for i in s if i!=' ']
    res = '#'
    for i in l1:
        res+=i
    return res

print(generate_hashtag('code wars'))