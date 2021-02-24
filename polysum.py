import math


def polysum(n, s):
    area = (0.25 * n * s**2) / math.tan(math.pi / n)
    perimeter = (s * n)**2
    result = perimeter + area
    return round(result, 4)


print(polysum(18, 23))