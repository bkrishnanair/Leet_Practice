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