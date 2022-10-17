from collections import Counter


def find_anagrams(text, pattern):
    """
    Find positions of anagrams pattern in text, case sensitive.
    Complexity: O(n)

    Args:
        text (str): string to search for anagrams
        pattern (str): pattern(without spaces) for anogram search

    Returns:
        anagrams_positions (list): list of anagrams positions
    """
    if len(pattern) > len(text):
        return []

    pattern_last_letter_pos = len(pattern) - 1
    counter_pattern = Counter(pattern)
    counter_string = Counter(text[:pattern_last_letter_pos])
    anagrams_positions = []
    for i, letter in enumerate(text[pattern_last_letter_pos:]):
        counter_string[letter] += 1
        if counter_string == counter_pattern:
            anagrams_positions.append(i)
        counter_string[text[i]] -= 1
        if counter_string[text[i]] == 0:
            del counter_string[text[i]]

    return anagrams_positions
