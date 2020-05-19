def getCount(inputStr):
    num_vowels = 0
    # your code here
    count = 0

    if len(inputStr) == 0:
        return num_vowels
    else:
        for element in range(0, len(inputStr)):
            if inputStr[element] == 'a':
                count = count + 1
            elif inputStr[element] == 'e':
                count = count + 1
            elif inputStr[element] == 'i':
                count = count + 1
            elif inputStr[element] == 'o':
                count = count + 1
            elif inputStr[element] == 'u':
                count = count + 1
    return count

    # return num_vowels

print(getCount(""))
print(getCount("abracadabra"))