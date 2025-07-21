class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)

        distinct_1 = list(set1 - set2)
        distinct_2 = list(set2 - set1)

        return [distinct_1, distinct_2]
'''

Convert to Sets: Instead of working with the lists directly, we'll first convert nums1 and nums2 into sets. This immediately takes care of any duplicate numbers within the original arrays.

Find the Difference: The core of the problem is finding elements in one collection that aren't in another. Sets have a built-in "difference" operation (using the - operator) that does exactly this.

set1 - set2 will give us all the unique elements that are in set1 but not in set2.

set2 - set1 will give us the unique elements in set2 but not in set1.

Return the Result: The problem asks for a list of lists, so we just convert the resulting difference sets back into lists.

Python Solution
This solution is in O(m + n) time complexity, where m and n are the lengths of the two arrays, because we iterate through each list once to create the sets. The space complexity is also O(m + n) to store the sets.

'''