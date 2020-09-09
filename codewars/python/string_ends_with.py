def solution(string, ending):
    #print(string)
    #print(string[len(string)-len(ending):len(string)])
    if string[len(string)-len(ending):len(string)] == ending:
        return bool(True)
    else: 
        return bool(False)


print(solution('abc', 'bc'))
print(solution('abc', 'd'))
print(solution('abcde', 'cde'))
print(solution('abcde', 'abc'))
print(solution('abcde', ''))

'''
https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d/train/python

def solution(string, ending):
    return string.endswith(ending)
'''
