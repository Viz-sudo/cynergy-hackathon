def toInt(s):
    curr = 0
    Dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    for i,j in zip(s,s[1:]):
        if Dict[i] < Dict[j]:
            curr -= Dict[i]
        else:
            curr += Dict[i]

    return curr + Dict[s[-1]]

def addTwoStrings(x,y):
    return (toInt(x) + toInt(y))

def convertBack(num):
    curr = 0
    Dict2 = { 1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
    for i,j in zip(num,num[1:]):
        if Dict2[i] < Dict2[j]:
            curr -= Dict2[i]
        else:
            curr += Dict2[i]

    return curr + Dict2[num[-1]]
