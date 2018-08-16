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
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('output.log')
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)


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
    b = x[len(x)//2:]
    c = y[:len(y)//2]
    d = y[len(y)//2:]
    
    logger.info('Divided x(%s) into a(%s) and b(%s)',x,a,b)
    logger.info('Divided y(%s) into c(%s) and d(%s)',y,c,d)

    n = len(x)

    try:
        ac = product(a, c)
        logger.info('Product(a,c): %s, %s = %s',a,c,ac)
    except(SystemExit, KeyboardInterrupt):
        raise
    except Exception:
        logger.error('Cannot compute ac', exc_info=True)

    try:
        bd = product(b, d)
        logger.info('Product(b,d): %s, %s = %s',b,d,bd)
    except(SystemExit, KeyboardInterrupt):
        raise
    except Exception:
        logger.error('Cannot compute bd', exc_info=True)

    p = int(a) + int(b)
    logger.info('p = a + b = %s + %s = %s',a,b,p)

    q = int(c) + int(d)
    logger.info('q = c + d = %s + %s = %s',c,d,q)

    try:
        pq = product(str(p), str(q))
        logger.info('pq = product(p, q) = %s, %s = %s',p,q,pq)
    except(SystemExit, KeyboardInterrupt):
        raise
    except Exception:
        logger.error('Cannot compute pq', exc_info=True)

    adbc = pq - ac - bd
    logger.info('adbc = pq-ac-bd = %s-%s-%s = %s',pq,ac,bd,adbc)

    result = (10**n * ac) + (10**(n//2) * adbc) + bd
    logger.info('Result: %s',result)
    return result

def main():
    x = input('Enter the 1st number: ')
    y = input('Enter the 2nd number: ')
    logger.info('Algorithm started with numbers x(%s) and y(%s)',x,y)

    start_time = datetime.now()

    x,y = zero_pad(x, y)
    logger.info('Corrected numbers to same n-length: x(%s) and y(%s)',x,y)

    result = product(x, y)
    print('Result: {}'.format(result))

    logger.info('Algorithm end time')
    end_time = (datetime.now() - start_time).total_seconds()
    print('Running time: {}'.format(end_time))

if __name__ == '__main__':
    main()

