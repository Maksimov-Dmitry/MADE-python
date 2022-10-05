"""
This module contains the CustomList class
"""

from itertools import zip_longest


class CustomList(list):
    """
    This class inherits the properties and methods from list.
    The following operators have been redefined:
        1. CustomList +/- CustomList
        2. CustomList +/- list
        3. list +/- CustomList
        4. CustomList compare CustomList (==, !=, <, <=, >, >=)
        5. str(CustomList)
    """

    def __add__(self, other):
        new_lst = [x + y for x, y in zip_longest(self, other, fillvalue=0)]
        return CustomList(new_lst)

    def __sub__(self, other, is_radd=False):
        new_lst = [y - x if is_radd else x - y
                   for x, y in zip_longest(self, other, fillvalue=0)]
        return CustomList(new_lst)

    def __radd__(self, other):
        return self.__add__(other)

    def __rsub__(self, other):
        return self.__sub__(other, is_radd=True)

    def __lt__(self, other):
        return sum(self) < sum(other)

    def __le__(self, other):
        return sum(self) <= sum(other)

    def __eq__(self, other):
        return sum(self) == sum(other)

    def __ne__(self, other):
        return sum(self) != sum(other)

    def __gt__(self, other):
        return sum(self) > sum(other)

    def __ge__(self, other):
        return sum(self) >= sum(other)

    def __str__(self):
        str_arr = ", ".join(str(elem) for elem in self)
        return f'[{str_arr}], {sum(self)}'
