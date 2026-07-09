from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Map to store: number -> its index
        seen = {}
        
        for index, num in enumerate(nums):
            complement = target - num
            
            # Look backward: if we already saw the complement, we found our pair
            if complement in seen:
                return [seen[complement], index]
            
            # Otherwise, remember this number and its index for future steps
            seen[num] = index