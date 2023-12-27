def valid_parentheses(string):
    if '(' and ')' not in string:
        return True
    if '(' in string and ')' not in string or ')' in string and '(' not in string:
        return False
    if string.count('(')!= string.count(')'):
            return False
    if string.count('(')== string.count(')'):
            if string[0]==')' or string[-1] == '(':
                return False
    else:
        return True


print(valid_parentheses('helo'))
print(valid_parentheses("hi())("))