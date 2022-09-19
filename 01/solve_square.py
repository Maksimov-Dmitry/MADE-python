from math import sqrt


def get_roots_of_quadratic_equation(a, b, c):
    if a == 0:
        return None
    D = b**2 - 4*a*c
    if D < 0:
        return None
    x1 = (-b + sqrt(D)) / (2*a)
    x2 = (-b - sqrt(D)) / (2*a)
    return x1, x2


def split_into_even_and_odd(array):
    evens = []
    odds = []
    for number in array:
        if isinstance(number, int):
            if number % 2 == 0:
                evens.append(number)
            else:
                odds.append(number)
        if isinstance(number, float):
            if int(number) == number:
                if int(number) % 2 == 0:
                    evens.append(number)
                else:
                    odds.append(number)
    return evens, odds


assert (1, -3) == get_roots_of_quadratic_equation(1, 2, -3)
assert (1, -5/2) == get_roots_of_quadratic_equation(2, 3, -5)
assert (5/2, -1) == get_roots_of_quadratic_equation(2, -3, -5)
assert (1, 1) == get_roots_of_quadratic_equation(1, -2, 1)
assert (4, 3) == get_roots_of_quadratic_equation(1, -7, 12)
assert (10.39, -0.39) == tuple(round(x, 2) for x in get_roots_of_quadratic_equation(3, -30, -12))
assert (10.39, -0.39) == tuple(round(x, 2) for x in get_roots_of_quadratic_equation(0.3, -3, -1.2))
assert (2, -2) == get_roots_of_quadratic_equation(2, 0, -8)
assert (3/2, 0) == get_roots_of_quadratic_equation(2, -3, 0)
assert (0, 0) == get_roots_of_quadratic_equation(2, 0, 0)
assert None == get_roots_of_quadratic_equation(0, 2, 3) #not quadratic equation
assert None == get_roots_of_quadratic_equation(1, -6, 13)

assert ([-2, 4, 0], [1, 3]) == split_into_even_and_odd([1, -2, 4, 3, 0])
assert ([-2., 4.], [1., 3.]) == split_into_even_and_odd([1., -2., 4., 3.])
assert ([2.], [1, 3.]) == split_into_even_and_odd([1, 2., 4.1, 3.])
assert ([2, 4], []) == split_into_even_and_odd([2, 4])
assert ([], [1, 3]) == split_into_even_and_odd([1, 3])
assert ([], []) == split_into_even_and_odd([])

print('All tests passed')