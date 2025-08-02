class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        max_length = 0
        zero_count = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1
            
            # If we have more than k zeros, move the left pointer
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            
            # Update the maximum length of the window
            max_length = max(max_length, right - left + 1)

        return max_length

# we are finding a window with k number of zero by sliding accross and the comapring window sizes to max window sizes


#To solve the problem of finding the maximum number of consecutive 1's in a binary array nums when you can flip at most k 0's, you can use the sliding window technique. Here's a step-by-step explanation of how to implement this:

# Initialize Variables: Use two pointers to represent the current window of 1's and 0's. Also, maintain a count of the number of 0's in the current window.

# Expand the Window: Move the right pointer to expand the window. If you encounter a 0, increment the count of 0's.

# Shrink the Window: If the count of 0's exceeds k, move the left pointer to shrink the window until the count of 0's is less than or equal to k.

# Calculate the Maximum: Throughout the process, keep track of the maximum length of the window that contains at most k 0's.