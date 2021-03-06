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
    # Otherwise add leading zeroes

    if len(x) < len(y):
        logger.info('%s < %s. Correcting length of %s',x,y,x)
        x = (len(y) - len(x)) * '0' + x

    elif len(y) < len(x):
        logger.info('%s < %s. Correcting length of %s',y,x,y)
        y = (len(x) - len(y)) * '0' + y

    if len(x) == len(y) and len(x) % 2 == 1:
        # checks if len(x) and len(y) is odd
        logger.info('Length of %s and %s is odd. Correcting to even',x,y)
        x = '0' + x
        y = '0' + y

    return x,y

def product(x, y):
    if len(x) == 1 and len(y) == 1:
        logger.info('%s and %s are same length. Return %s * %s',x,y,x,y)
        return int(x) * int(y)

    x,y = zero_pad(x,y)

    a = x[:len(x)//2]
    b = x[len(x)//2:]
    c = y[:len(y)//2]
    d = y[len(y)//2:]
    
    logger.info('Divided (%s) into a(%s) and b(%s)',x,a,b)
    logger.info('Divided (%s) into c(%s) and d(%s)',y,c,d)

    n = len(x)

    try:
        logger.info('Compute ac = product(%s, %s)',a,c)
        ac = product(a, c)
        logger.info('Product(a,c): %s, %s = %s',a,c,ac)

    except(SystemExit, KeyboardInterrupt):
        raise
    except Exception:
        logger.error('Cannot compute ac', exc_info=True)

    try:
        logger.info('Compute bd = product(%s, %s)',b,d)
        bd = product(b, d)
        logger.info('Product(b,d): %s, %s = %s',b,d,bd)

    except(SystemExit, KeyboardInterrupt):
        raise
    except Exception:
        logger.error('Cannot compute bd', exc_info=True)

    logger.info('Compute p = %s+%s',a,b)
    p = int(a) + int(b)
    logger.info('p = a + b = %s + %s = %s',a,b,p)

    logger.info('Compute q = %s+%s',c,d)
    q = int(c) + int(d)
    logger.info('q = c + d = %s + %s = %s',c,d,q)

    try:
        logger.info('Compute pq = product(%s, %s)',p,q)
        pq = product(str(p), str(q))
        logger.info('pq = product(%s, %s) = %s',p,q,pq)

    except(SystemExit, KeyboardInterrupt):
        raise
    except Exception:
        logger.error('Cannot compute pq', exc_info=True)

    logger.info('Compute adbc = %s-%s-%s',pq,ac,bd)
    adbc = pq - ac - bd
    logger.info('adbc = pq-ac-bd = %s-%s-%s = %s',pq,ac,bd,adbc)

    logger.info('Compute Karatsuba')
    logger.info('(10^%s * %s) + (10^(%s/2) * %s) + %s',n,ac,n,adbc,bd)
    result = (10**n * ac) + (10**(n//2) * adbc) + bd

    logger.info('Karatsuba product(%s, %s) = %s',x,y,result)
    return result

def main():
    x = input('Enter the 1st number: ')
    y = input('Enter the 2nd number: ')
    logger.info('Algorithm started with numbers x(%s) and y(%s)',x,y)

    start_time = datetime.now()

    result = product(x, y)
    print('Result: {}'.format(result))

    logger.info('Algorithm end time')
    end_time = (datetime.now() - start_time).total_seconds()
    print('Running time: {}'.format(end_time))

    assert product(str(32),str(767)) == 24544, "Incorrect product computation"
    assert product(str(123456789),str(123456789)) == 15241578750190521, "Incorrect product computation"

if __name__ == '__main__':
    main()

