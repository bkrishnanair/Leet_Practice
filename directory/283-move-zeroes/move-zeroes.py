class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=0
        for i in range(len(nums)):
            if nums[i] != 0:
               nums[l], nums[i] = nums[i], nums[l]
               l+=1

# Initialize a pointer l to keep track of the position to place the next non-zero element.
# Iterate over each element in the list.
# If the current element is not zero, swap it with the element at position l and then increment l.This approach ensures that all non-zero elements are moved to the front of the list, and all zeros are moved to the end.
        