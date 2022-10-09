class LRUCache:
    """
    This is Least Recently Used (LRU) Cache class.

    Args:
        limit (int): The max size of LRUCache structure

    Raises:
        ValueError: Limit must be integer and >= 1)
    """

    def __init__(self, limit=42):
        if not isinstance(limit, int) or limit < 1:
            raise ValueError(f'Limit must be integer and >= 1, was {limit}.')

        self.__limit = limit
        self._data = {}

    def get(self, key):
        """
        Get value given key. Complexity: O(n)

        Args:
            key: key to get a value

        Returns:
            val: a value given key, None if key doesn't exist
        """

        if key not in self._data:
            return None

        val = self._data.pop(key)  # delete an item to make it last
        self._data[key] = val
        return val

    def set(self, key, value):
        """
        Set key and corresponding value. Complexity: O(n)

        Args:
            key: key to set
            value: value to set
        """

        if key in self._data:
            self._data.pop(key)  # delete an item to make it last
            self._data[key] = value
        else:
            if len(self._data) == self.__limit:
                # delete a first item via iterator
                self._data.pop(next(iter(self._data)))
            self._data[key] = value

    @property
    def data(self):
        return self._data
