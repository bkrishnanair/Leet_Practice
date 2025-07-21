class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
              candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate
        

'''
using the Boyer-Moore Voting Algorithm, which is designed specifically for this problem and meets the follow-up constraints.

The Logic (Boyer-Moore Algorithm)
The algorithm works by maintaining a count and a candidate element. Think of it like a vote:

We start with a count of 0 and no candidate.

Iterate through the array. If the count is 0, we nominate the current number as the new candidate.

If the current number is the same as our candidate, we increment the count (a vote for the candidate).

If the current number is different, we decrement the count (a vote against the candidate).

'''