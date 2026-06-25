def freq_counter(arr):
    """Return a dictionary with frequency of each integer in arr."""
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return freq


def most_frequent_element(freq_dict):
    """Return the element with the highest frequency."""
    max_count = -1
    most_freq = None

    for num, count in freq_dict.items():
        if count > max_count:
            max_count = count
            most_freq = num

    return most_freq, max_count


def elements_appearing_once(freq_dict):
    """Return a list of elements that appear exactly once."""
    once = []
    for num, count in freq_dict.items():
        if count == 1:
            once.append(num)
    return once
