def divisors(n):
    count = 0
    for i in range(1,n+1):
        if n%i == 0:
            count += 1

    return count
print(divisors(4))
print(divisors(5))
print(divisors(12))
print(divisors(30))

'''
https://www.codewars.com/kata/542c0f198e077084c0000c2e/train/python

def divisors(n):
    return  len([l_div for l_div in range(1, n + 1) if n % l_div == 0]);
'''
