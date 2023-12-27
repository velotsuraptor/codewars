def solution(string, ending):
    string = string[::-1]
    sliced = string[:len(ending)]
    sliced = sliced[::-1]
    if sliced == ending:
        return True
    else:
        return False


print(solution('abcde', 'cde'))
