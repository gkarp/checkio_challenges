'''
https://www.codewars.com/kata/scramblies
Write function scramble(str1,str2) that returns true if a portion of str1
characters can be rearranged to match str2, otherwise returns false.

For example:
str1 is 'rkqodlw' and str2 is 'world' the output should return true.
str1 is 'cedewaraaossoqqyt' and str2 is 'codewars' should return true.
str1 is 'katas' and str2 is 'steak' should return false.

Only lower case letters will be used (a-z). No punctuation or digits
will be included.
Performance needs to be considered
'''
def scramble(str1, str2):
    # iterate through each character in str2
    for c in str2:
        i = 0
        if c not in str1:
            return False
        for char in str1:
            if char == c:
                # remove c from str2 and char from str1 and continue thru str2
                str1 = str1[0:i] + str1[i + 1:len(str1)]
                str2 = str2[1:len(str2)]
                break
            i += 1
            # if not able to find c after iterating through str1 return False
            #if i == len(str1):
                #return False
    return True

print(scramble('rkqodlw', 'world') == 1)
print(scramble('cedewaraaossoqqyt', 'codewars') == 1)
print(scramble('katas', 'steak') == 1)
print(scramble('scriptjava','javascript'))
print(scramble('scriptingjava','javascript'))
print(scramble('katas', 'z') == 1)
print(scramble('zxq', 'bdeds') == 1)
print(scramble('ufuewn', 'new') == 1)
