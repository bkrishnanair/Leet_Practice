from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # Calculate the total sum of the array
        total_sum = sum(nums)
        
        # Initialize left_sum to 0 to store the sum of elements to the left of the pivot
        left_sum = 0

        # Iterate through the array to find the pivot index
        for i, num in enumerate(nums):
            # If left_sum equals the sum of elements to the right of the pivot, return the index
            if left_sum == (total_sum - left_sum - num):
                return i
            # Update left_sum to include the current element
            left_sum += num

        # If no pivot index is found, return -1
        return -1



#There are a few issues with the current implementation, such as iterating over the list and calculating sums.


# class Solution:
#     def pivotIndex(self, nums: List[int]) -> int:
        
#         l = len(nums)
#         pivot_index = 0
#         count = 0

#         for i in range(nums):
#             if sum[:i-1] == sum[i+1:l-1]:
#                 pivot_index = i
#                 i=+1
#         return i



