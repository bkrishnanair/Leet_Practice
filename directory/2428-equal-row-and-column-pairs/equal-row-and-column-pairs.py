from typing import List
from collections import Counter

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # Initialize a counter for the final result.
        count = 0
        n = len(grid)
        
        # Step 1: Count the frequency of each unique row.
        # We convert each row (list) to a tuple to make it hashable for the Counter key.
        # e.g., {(3, 2, 1): 1, (1, 7, 6): 1, (2, 7, 7): 1}
        row_counts = Counter(tuple(row) for row in grid)
        
        # Step 2: Iterate through each column and check for matches.
        for j in range(n):
            # Construct the current column as a tuple.
            current_col = []
            for i in range(n):
                current_col.append(grid[i][j])
            current_col_tuple = tuple(current_col)
            
            # If this column pattern exists in our row_counts map,
            # add the number of times it appeared as a row to our count.
            # Counter returns 0 if the key is not found, so this is safe.
            count += row_counts[current_col_tuple]
            
        return count


        '''
        didnt get it
        '''
