"""
This module tests the CustomList class
"""

from custom_list import CustomList


def is_customlist_as_list(custom_list, lst):
    """
    Help function to compare list and CustomList
    """
    return all(i == j for i, j in zip(custom_list, lst))


CustomList_A = CustomList([5, 1, 3, 7])
CustomList_B = CustomList([1, 2, 7])


CustomList_sum = CustomList_A + CustomList_B
assert is_customlist_as_list(CustomList_sum, [6, 3, 10, 7])
assert is_customlist_as_list(CustomList_A, [5, 1, 3, 7])
assert is_customlist_as_list(CustomList_B, [1, 2, 7])
assert isinstance(CustomList_sum, CustomList)

CustomList_sub = CustomList_A - CustomList_B
assert is_customlist_as_list(CustomList_sub, [4, -1, -4, 7])
assert is_customlist_as_list(CustomList_A, [5, 1, 3, 7])
assert is_customlist_as_list(CustomList_B, [1, 2, 7])
assert isinstance(CustomList_sub, CustomList)

List_add_CustomList = [2, 3] + CustomList_B
assert is_customlist_as_list(List_add_CustomList, [3, 5, 7])
assert is_customlist_as_list(CustomList_B, [1, 2, 7])
assert isinstance(List_add_CustomList, CustomList)

CustomList_add_List = CustomList_A + [2, 3]
assert is_customlist_as_list(CustomList_add_List, [7, 4, 3, 7])
assert is_customlist_as_list(CustomList_A, [5, 1, 3, 7])
assert isinstance(CustomList_add_List, CustomList)

List_sub_CustomList = [2, 3] - CustomList_A
assert is_customlist_as_list(List_sub_CustomList, [-3, 2, -3, -7])
assert is_customlist_as_list(CustomList_A, [5, 1, 3, 7])
assert isinstance(List_sub_CustomList, CustomList)

CustomList_sub_List = CustomList_B - [2, 3]
assert is_customlist_as_list(CustomList_sub_List, [-1, -1, 7])
assert is_customlist_as_list(CustomList_B, [1, 2, 7])
assert isinstance(List_sub_CustomList, CustomList)

assert CustomList_B < CustomList_A
assert CustomList_B <= CustomList_A
assert CustomList_B == CustomList([8, 2])
assert CustomList_A > CustomList_B
assert CustomList_A >= CustomList_B

assert str(CustomList_B) == '[1, 2, 7], 10'
