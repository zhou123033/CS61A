# Print
-2
print(-2)
print(1, 2, 3)
x = -2
x
print(x)
x = print(-2)
x
print(x)

None
1
"hi"
abs

print(None)
print(1, 2, 3)
print(None, None)
print(print(1), print(2))

# Division
618 / 10
618 // 10
618 % 10
from operator import truediv, floordiv, mod

floordiv(618, 10)
truediv(618, 10)
mod(618, 10)

# Approximation
5 / 3
5 // 3
5 % 3


# Multiple return values
def divide_exact(n, d):
    return n // d, n % d


quotient, remainder = divide_exact(618, 10)


# Dostrings, doctests, & default arguments
def divide_exact(n, d=10):
    """Return the quotient and remainder of dividing N by D.

    >>> quotient, remainder = divide_exact(618, 10)
    >>> quotient
    61
    >>> remainder
    8
    """
    return floordiv(n, d), mod(n, d)


# Conditional expressions
def absolute_value(x):
    """Return the absolute value of X.

    >>> absolute_value(-3)
    3
    >>> absolute_value(0)
    0
    >>> absolute_value(3)
    3
    """
    if x < 0:
        return -x
    elif x == 0:
        return 0
    else:
        return x


# Summation via while
i, total = 0, 0
while i < 3:
    i = i + 1
    total = total + i
print("i:", i, "total:", total)


# Prime factorization
def prime_factors(n):
    """Print the prime factors of positive integer n
       in non-decreasing order.

    >>> prime_factors(8)
    2
    2
    2
    >>> prime_factors(9)
    3
    3
    >>> prime_factors(10)
    2
    5
    >>> prime_factors(11)
    11
    >>> prime_factors(12)
    2
    2
    3
    >>> prime_factors(858)
    2
    3
    11
    13
    """
    while n > 1:
        k = smallest_factor(n)
        print(k)
        n = n // k


def smallest_factor(n):
    """Return the smallest factor of n greater than 1."""
    k = 2
    while n % k != 0:
        k = k + 1
    return k
