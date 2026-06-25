
def two_sum(nums, target):
    """
    Return indices [i, j] such that nums[i] + nums[j] == target.

    The 'complement' is the number we still need to reach the target.
    For each num, complement = target - num.
    We store complements in a hash map so we can find matches in O(1) average time.
    """
    seen = {}  # value -> index

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i

    return []
