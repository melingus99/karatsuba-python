# Karatsuba Algorithm in Python

This is a work in progress. I am implementing Karatsuba algorithm in Python.

**Input**: Two n-digit integers `x`, `y`
**Output**: The product `x * y`

**8/16/18**: Not computing the right result.

## Base case:

If `n=1` then compute the product in one step

## Recursive case:

...else

    a,b := left and right sides of x
    c,d := left and right sides of y

The product `x * y` is calculated like this:

    10^(n) ac + 10^(n/2) (ad + bc) + bd

* Recursive compute: `ac := a*c`
* Recursive compute: `bd := b*d`
* Compute: `(a+b)*(c+d) = ac+ad+bc+bd`
* Compute: `p := a+b`
* Compute: `q := c+d`
* Recursive compute: `pq := p*q`
* Compute: `adbc := pq - ac -bd`
* Compute: Big formula

## The formula

This is where the formula comes from

    x = 10^(n/2) a + b
    y = 10^(n/2) c + d

Which means an `n-digit` number can be expressed in such way.

Example:

    x = 425
    n = 3

To divide the number `x` in two parts. We can a leading zero.

    x = 0425
    a = 04
    b = 25

Using the formula:

    x = 10^(n/2) a + b
    x = 10^(4/2) 04 + 25
    x = 10^(2) 04 + 25
    x = 100 * 04 + 25
    x = 400 + 25
    x = 425

Now multiply `x` and `y` using such formulas:

    x = 10^(n/2) a + b
    y = 10^(n/2) c + d
    x * y = (10^(n/2) a + b)(10^(n/2) c + d)
    x * y = (10^(n/2) a * 10^(n/2) c) +
            (10^(n/2) a * d) +
	    (10^(n/2) c * b) +
	    (b * d)
	  = 10^(n) ac + 10^(n/2) ad + 10^(n/2) cb + bd
	  = 10^(n) ac + 10^(n/2) (ad+bc) + bd

## Recursive case computations

The product `x * y` is calculated like this:

10^(n) ac + 10^(n/2) (ad + bc) + bd

* Recursive compute: `ac := a*c`
* Recursive compute: `bd := b*d`

Compute: `(a+b)*(c+d) = ac+ad+bc+bd` like this:

* Compute: `p := a+b`
* Compute: `q := c+d`
* Recursive compute: `pq := p*q`

Compute: `(ad+bc)` like this:

* Compute: `adbc := pq - ac -bd`

Finally, compute the Big formula.

It looks like the Big formula uses 4 recursive multiplications:

* ac
* ad
* bc
* bd

But the recursive computations can be reduced to 3. Instead of computing `ad` and `bc` we are following these steps:

1. ac
2. pq
3. bd

## Algorithm running time

Using the Master Theorem:

    T(n) = 3T(n/2) + O(n)
    T(n) = O(n log2 3)
    T(n) = O(n^1.584)

This comes from the formula:

    T(n) = aT(n/b) + f(n)

where:

* `T(n)`: algoritm running time
* `n`: size of the input
* `a`: number of subproblems in the recursion
* `b`: factor by which the subproblem size is reduced ine each recursive call.
* `f(n)`: "the amount of time taken at the top level of the recurrence" (Wikipedia). To me it means the time outside of the recursive calls.

From the algorithm using 3 recursive calls:

* `a = 3` recursive calls
* `b = 2`. For every recursive call, the number is reduced by half
* `f(n) = 4 O(n) = O(n)`

`f(n) = 4 O(n)` comes from:

* Compute `p := a+b`
* Compute `q := c+d`
* Compute `adbc := pq - ac - bd`
* Compute `10^n ac + 10^n/2 adbc + bd`

## Troubleshooting

**8/15/18**: The code is not complete. I am getting errors on the recursive calls.

    ac = product(a, c)
    [Previous line repeated 989 more times]
    File "karatsuba.py", in product
      print(a)
    RecursionError: maximum recursion depth
    exceeded while calling a Python object

**8/16/18**: I added logging everywhere. Not exactly sure what I did. But the error doesn't show up on stdout anymore.
