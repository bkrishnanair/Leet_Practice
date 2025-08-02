from typing import List
from collections import Counter

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # Create a counter for the numbers in the array.
        count = Counter(nums)
        operations = 0

        # The main loop iterates through each number in the original list.
for num in nums:
    # Calculate the number needed to sum to k.
    complement = k - num

    # Check if the current number and its complement are available.
    if count[num] > 0 and count[complement] > 0:
        # Special case: If the number is its own complement (e.g., k=6, num=3).
        if num == complement and count[num] < 2:
            # If there aren't at least two of the same number, we can't form a pair.
            # We skip this number and continue to the next one.
            continue
        
        # If we found a valid pair, perform an operation.
        operations += 1
        # Decrement the count for both numbers to show they have been "used".
        count[num] -= 1
        count[complement] -= 1