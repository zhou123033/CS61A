from operator import add, mul

square = lambda x: x * x

identity = lambda x: x

triple = lambda x: 3 * x

increment = lambda x: x + 1

def funception(func1, start):
    """ Takes in a function (function 1) and a start value.
    Returns a function (function 2) that will find the product of
    function 1 applied to the range of numbers from
    start (inclusive) to stop (exclusive)

    >>> def func1(num):
    ...     return num + 1
    >>> func2_1 = funception(func1, 0)
    >>> func2_1(3)    # func1(0) * func1(1) * func1(2) = 1 * 2 * 3 = 6
    6
    >>> func2_2 = funception(func1, 1)
    >>> func2_2(4)    # func1(1) * func1(2) * func1(3) = 2 * 3 * 4 = 24
    24
    >>> func2_3 = funception(func1, 3)
    >>> func2_3(2)    # Returns func1(3) since start >= stop
    4
    >>> func2_4 = funception(func1, 3)
    >>> func2_4(3)    # Returns func1(3) since start >= stop
    4
    >>> func2_5 = funception(func1, -2)
    >>> func2_5(-3)    # Returns None since start < 0
    >>> func2_6 = funception(func1, -1)
    >>> func2_6(4)    # Returns None since start < 0
    """
    def func2(stop):
        total = 1
        if start < 0:
            return None
        if start >= stop:
            return func1(start)
        for i in range(start, stop):
            total = total * func1(i)
        return total
    return func2