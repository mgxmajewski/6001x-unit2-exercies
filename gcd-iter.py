def gcdIter(a, b):
    """
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    """
    # Your code here
    if a == b:
        return a
    elif a > b:
        temp = b
        for i in range(a):
            if a % b == 0 and temp % b == 0:
                return b
            else:
                b -= 1
    elif a < b:
        temp = a
        for i in range(b):
            if b % a == 0 and temp % a == 0:
                return a
            else:
                a -= 1


print(gcdIter(35, 60))
