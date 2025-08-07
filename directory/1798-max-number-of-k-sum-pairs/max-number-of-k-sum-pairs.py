from typing import List
from collections import Counter

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # Create a counter for the numbers in the array.
        count = Counter(nums)
        operations = 0
        for num in nums:
            # Check if the complement (k - num) exists in the counter.
            complement = k - num
            if count[num] > 0 and count[complement] > 0:
                # If the number and its complement are the same, ensure there are at least two instances.
                if num == complement and count[num] < 2:
                    continue
                # Increment operations and decrement the count of the number and its complement.
                operations += 1
                count[num] -= 1
                count[complement] -= 1
        return operations

