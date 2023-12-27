def is_anagram(test, original):
    if sorted(test) == sorted(original):
        return True

print(is_anagram('maria','irama'))