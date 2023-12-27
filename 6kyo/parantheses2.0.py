def valid_parentheses(string):
    l = [i for i in string]
    for i in l:
        if i =='(':
            l = l.remove(i)
            if ')' in l:
                l = l.remove(')')
    if '(' or ')' in l:
        return False
    if '(' or')' not in l:
        return True


print(valid_parentheses('helo'))
print(valid_parentheses("hi())("))
print(valid_parentheses('hi())('))