class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        prev1, prev2 = 2, 1  # Initialize for n=2 and n=1 cases
        
        for i in range(3, n + 1):
            curr = prev1 + prev2  # Compute ways for current step
            prev2 = prev1  # Move previous values forward
            prev1 = curr
        
        return prev1


# #- prev1 → Stores the number of ways to reach step (n-1).
# - prev2 → Stores the number of ways to reach step (n-2).
# At the end of the loop, prev1 holds the total ways to climb n steps (n=5 → 8 ways).
