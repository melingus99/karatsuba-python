# Karatsuba
# input: two positive integers x,y with n-digits
# output: the product x*y
# assume: n is a power of 2
#
# Base case:
# if n=1 then compute x*y in one step
# - Ex: x=1, y=3. x*y = 1*3 = 3
# 
# Recursive case:
# else
# - 10^n ac + 10^n/2 (ad+bc) + bd
# - a := left side of x, b := right side of x
# - c := left side of y, d := right side of y
#       a  b
#   *   c  d
#      -----
#      ad  ab
# + ac bc
# -----------
#  ac  0   0
# +  ad+bc 0
# +        ab
# -----------
# ac ad+bc ab
#
# - Recursive compute ac := a*c
# - Recursive compute bd := b*d
# - Compute (a+b)*(c+d) = ac+ad+bc+bd
# - p := a+b, q := c+d
# - Recursive compute pq := p*q
# - Compute adbc := pq - ac - bd
# - Compute 10^n ac + 10^n/2 adbc + bd

from datetime import datetime
import sys

def zero_pad(x, y):
    # Numbers have to be of same length n
    # Otherwise add trailing zeroes

    if len(x) < len(y):
        x = (len(y) - len(x)) * '0' + x
    elif len(y) < len(x):
        y = (len(x) - len(y)) * '0' + y

    return x,y

def product(x, y):
    if len(x) == 1 and len(y) == 1:
        return int(x) * int(y)
    elif len(x) != len(y):
        zero_pad(x,y)

    a = x[:len(x)//2]
    print(a)
    b = x[len(x)//2:]
    print(b)
    c = y[:len(y)//2]
    print(c)
    d = y[len(y)//2:]
    print(d)

    n = len(x)
    print(n)

    ac = product(a, c)
    print(ac)

    bd = product(b, d)
    print(bd)

    p = int(a) + int(b)
    print(p)
    q = int(c) + int(d)
    print(q)

    pq = product(str(p), str(q))
    print(pq)

    adbc = pq - ac - bd
    print(adbc)

    result = (10**n * ac) + (10**(n//2) * adbc) + bd
    print(result)
    return result

def main():
    x = input('Enter the 1st number: ')
    y = input('Enter the 2nd number: ')
    start_time = datetime.now()

    x,y = zero_pad(x, y)
    print('Fixed numbers length: {}, {}'.format(x,y))

    result = product(x, y)
    print('Result: {}'.format(result))

    end_time = (datetime.now() - start_time).total_seconds()
    print('Running time: {}s'.format(end_time))

if __name__ == '__main__':
    main()

