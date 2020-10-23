# TODO: finish this kata

from re import search

# regex="[A-Za-z0-9]{6,}"
# regex="^.*(?=.{6,})(?=.*[a-zA-Z])(?=.*?[A-Z])(?=.*\d)[a-zA-Z0-9]+$"
regex="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d@$!#%*?&]{6,}$"

print(bool(search(regex, 'fjd3IR9')))
print(bool(search(regex, 'ghdfj32')))
print(bool(search(regex, 'DSJKHD23')))
print(bool(search(regex, 'dsF43')))
print(bool(search(regex, '4fdg5Fj3')))
print(bool(search(regex, 'DHSJdhjsU')))
print(bool(search(regex, 'fjd3IR9.;')))
print(bool(search(regex, 'fjd3  IR9')))
print(bool(search(regex, 'djI38D55')))
print(bool(search(regex, 'a2.d412')))
print(bool(search(regex, 'JHD5FJ53')))
print(bool(search(regex, '!fdjn345')))
print(bool(search(regex, 'jfkdfj3j')))
print(bool(search(regex, '123')))
print(bool(search(regex, 'abc')))
print(bool(search(regex, '123abcABC')))
print(bool(search(regex, 'ABC123abc')))
print(bool(search(regex, 'Password123')))
'''
https://www.codewars.com/kata/52e1476c8147a7547a000811/train/python
'''
