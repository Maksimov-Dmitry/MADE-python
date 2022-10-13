from collections import Counter


def find_anagrams(text, pattern):
    """
    Find positions of anagrams pattern in text, case sensitive.
    Complexity: O(n), n - number of words in text

    Args:
        text (str): string to search for anagrams
        pattern (str): pattern(without spaces) for anogram search

    Returns:
        anagrams_positions (list): list of anagrams positions
    """

    counter_pattern = Counter(pattern)
    anagrams_positions = []
    for i, word in enumerate(text.split()):
        if counter_pattern == Counter(word):
            anagrams_positions.append(i)

    return anagrams_positions
