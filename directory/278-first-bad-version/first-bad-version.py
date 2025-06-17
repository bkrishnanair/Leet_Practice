# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        
        while left < right:
            mid = (left + right) // 2  # Find middle version
            
            if isBadVersion(mid):
                right = mid  # Move to the left part to find earlier bad version
            else:
                left = mid + 1  # Move to the right part
                
        return left  # The first bad version