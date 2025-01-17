class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_sum = window_sum

        for i in range(k, len(nums)):
            window_sum = window_sum + nums[i] - nums[i-k]
            max_sum = max(max_sum, window_sum)

        return max_sum / k

# instead of avg just focus on sum as k is given, and use sliding window that is sum of first K then move the window by one element, comapre the sum obtain the max_sum through iteration form K th elemt to end
