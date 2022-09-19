def get_closest_to_zero(array):
    if not array:
        return []

    closest_values = [float("inf")]
    for value in array:
        if abs(value) <= abs(closest_values[0]):
            if abs(value) == abs(closest_values[0]):
                closest_values.append(value)
            else:
                closest_values = [value]
    return closest_values


def merge(arr1, arr2):
    """"
        Since we are going to use "in" very often we will transform second container into set, which uses the hash.
        Also, we will use a dictionary as a container to store the merged values, since dictionary is the order-preserving
         and the hash-based. Time complexity: O(n + m).
    """
    set_arr2 = set(arr2)
    res_dict = dict()
    for value in arr1:
        if value in set_arr2:
            res_dict[value] = None

    return list(res_dict.keys())


assert [0] == get_closest_to_zero([0])
assert [1] == get_closest_to_zero([2, 4, 1])
assert [-1.2, 1.2, -1.2] == get_closest_to_zero([1.3, 2, -1.2, 1.2, -1.2])
assert [] == get_closest_to_zero([])

assert [1, 2, 7] == merge([1, 1, 2, 5, 7], (1, 1, 2, 3, 4, 7))
assert [-2, 1, 7.2] == merge([-2, 1, 1, 5, 7.2], (-2, 1, 1, 2, 3, 4, 7.2))
assert [] == merge((1, 2,), [3, 4])
assert [] == merge([1, 2, 3], [])
assert [] == merge((), (1, 2, 3))
assert [] == merge([], [])

print('All tests passed')
