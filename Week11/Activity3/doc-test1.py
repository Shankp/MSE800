import doctest


def add(x, y):
    """
    Adds two numbers.
    >>> add(2, 3)
    5
    """
    return x + y


def Multiplication(x, y):
    """
    Multiplies two numbers.
    >>> Multiplication(2, 3)
    6
    """
    return x * y


def Division(x, y):
    """
    Divides two numbers.
    >>> Division(6, 3)
    2.0
    """
    return x / y


if __name__ == "__main__":
    doctest.testmod()
