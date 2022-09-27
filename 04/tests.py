"""
This module tests the CustomList class
"""

from custom_list import CustomList


CustomList_A = CustomList([5, 1, 3, 7])
CustomList_B = CustomList([1, 2, 7])

assert (CustomList_A + CustomList_B).lst == [6, 3, 10, 7]
assert isinstance(CustomList_A + CustomList_B) == CustomList

assert (CustomList_A - CustomList_B).lst == [4, -1, -4, 7]
assert isinstance(CustomList_A - CustomList_B) == CustomList

assert ([2, 3] + CustomList_B).lst == [3, 5, 7]
assert isinstance([2, 3] + CustomList_B) == CustomList

assert (CustomList_B + [2, 3]).lst == [3, 5, 7]
assert isinstance(CustomList_B + [2, 3]) == CustomList

assert ([2, 3] - CustomList_B).lst == [1, 1, -7]
assert isinstance([2, 3] - CustomList_B) == CustomList

assert (CustomList_B - [2, 3]).lst == [-1, -1, 7]
assert isinstance(CustomList_B - [2, 3]) == CustomList

assert CustomList_B < CustomList_A
assert CustomList_B <= CustomList_A
assert CustomList_B == CustomList([8, 2])
assert CustomList_A > CustomList_B
assert CustomList_A >= CustomList_B

assert str(CustomList_B) == '[1, 2, 7], 10'
