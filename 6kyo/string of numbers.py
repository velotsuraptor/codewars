def phone_words(string_of_nums):
    st = string_of_nums
    sums = {'Z': '9999', 'Y': '999', 'X': '99', 'W': '9', 'V': '888', 'U': '88', 'T': '8', 'S': '7777', 'R': '777',
            'Q': '77', 'P': '7', 'O': '666', 'N': '66', 'M': '6', 'L': '555', 'K': '55', 'J': '5', 'I': '444',
            'H': '44', 'G': '4', 'F': '333', 'E': '33', 'D': '3', 'C': '222', 'B': '22', 'A': '2'}
    s = st.split('0')
    vls = list(sums.values())
    for i in s:
        for j in vls:
            for k in i:
                i.replace(j, str(sums.get(j)))
    return s


print(phone_words("443355555566604466690277733099966688"))
