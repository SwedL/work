from itertools import groupby

KEYBOARD = {
    "1": "", "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
    "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz", "0": " "
}

def phone_words(str):
    ans = []
    for digit, sequence in filter(lambda x: x[0] != "1", groupby(str)):
        q, r = divmod(len(list(sequence)), len(KEYBOARD[digit]))
        if q: ans.append(KEYBOARD[digit][-1] * q)
        if r: ans.append(KEYBOARD[digit][r - 1])
        #print(digit, list(sequence))
    return "".join(ans)

print(phone_words("559991998888844033348809444444455444660555229988338855"))