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
    res_arr = list(set(arr1).intersection(arr2))
    
    return res_arr


assert [0] == get_closest_to_zero([0])
assert [1] == get_closest_to_zero([2, 4, 1])
assert [-1.2, 1.2, -1.2] == get_closest_to_zero([1.3, 2, -1.2, 1.2, -1.2])
assert [] == get_closest_to_zero([])

assert [1, 2, 7] == merge([1, 1, 2, 5, 7], (1, 1, 2, 3, 4, 7))
assert [] == merge((1, 2,), [3, 4])
assert [] == merge([1, 2, 3], [])
assert [] == merge((), (1, 2, 3))
assert [] == merge([], [])

print('All tests passed')
