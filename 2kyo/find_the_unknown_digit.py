from random import randint
def expr(exp):
    for i in exp[::-1]:
        for j in exp:
            if j == '?' or i == '?':
                exp = exp.replace(j, str(randint(0, 10)))
    return eval(exp)
def solve_runes(runes):
    rez = None
    runes = runes.replace('=','==')
    while rez != True:
        rez = expr(runes)
    return eval(runes)


'1 * 5 = 5\n2 * 5 = 10\n3 * 5 = 15\n4 * 5 = 20\n5 * 5 = 25\n6 * 5 = 30\n7 * 5 = 35\n8 * 5 = 40\n9 * 5 = 45' should equal
'1 * 5 = 5\n2 * 5 = 10\n3 * 5 = 15\n4 * 5 = 20\n5 * 5 = 25\n6 * 5 = 30\n7 * 5 = 35\n8 * 5 = 40\n9 * 5 = 45\n10 * 5 = 50'

print(solve_runes("123*45?=5?088"))