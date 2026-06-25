def is_anagram(s1, s2):
    """Return True if s1 and s2 are anagrams, False otherwise."""
    if len(s1) != len(s2):
        return False

    freq = {}

    for ch in s1:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    for ch in s2:
        if ch not in freq:
            return False
        freq[ch] -= 1
        if freq[ch] == 0:
            del freq[ch]

    return len(freq) == 0


def is_anagram_clean(s1, s2):
    """
    Bonus version:
    - removes spaces
    - converts both strings to lowercase
    """
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    return is_anagram(s1, s2)
