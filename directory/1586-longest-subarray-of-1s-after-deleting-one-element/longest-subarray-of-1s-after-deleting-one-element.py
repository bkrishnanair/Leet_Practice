from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        max_length = 0
        zero_count = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1
            
            # If we have more than one zero, move the left pointer
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            
            # Update the maximum length of the window
            # We subtract 1 because we need to delete one element
            max_length = max(max_length, right - left +1 -1)

        return max_length