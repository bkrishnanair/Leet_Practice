from typing import List
from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        freq_map = Counter(arr)
        occurrences = freq_map.values()
      
        return len(occurrences) == len(set(occurrences))


'''

# Step 1: Count the occurrences of each number using a Counter.
        # For arr = [1,2,2,1,1,3], freq_map will be {1: 3, 2: 2, 3: 1}
       
        
        # Step 2: Get a list of the occurrence counts.
        # For the example above, occurrences will be a view object like dict_values([3, 2, 1])

  
        # Step 3: Compare the number of counts with the number of *unique* counts.
        # A set only stores unique elements.
        # len(occurrences) is 3.
        # len(set(occurrences)) is also 3 (since {1, 2, 3} has 3 elements).
        # Since 3 == 3, we return True.
        # If arr was [1, 2], occurrences would be [1, 1].
        # len([1, 1]) is 2, but len(set([1, 1])) is 1. Since 2 != 1, it would return False.

'''

'''
Count Frequencies: The best way to count the occurrences of each number in the array is to use a hash map. We'll iterate through the array and store each number as a key and its frequency as the value. For example, [1, 2, 2, 1, 1, 3] becomes {1: 3, 2: 2, 3: 1}.

Check for Unique Counts: Now that we have the frequencies (3, 2, and 1 in our example), we need to check if these numbers are all unique. The easiest way to do this is to add them to a hash set, which automatically discards duplicates.

Compare Sizes: If the number of frequencies we found is equal to the size of our hash set, it means no frequencies were discarded, so they must all be unique. If the sizes are different, it means there was at least one duplicate frequency.

Python Solution
This solution uses Python's collections.Counter, a specialized dictionary subclass for counting hashable objects, which simplifies Step 1.
'''