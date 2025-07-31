class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count =0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                # Check if the left and right plots are empty.
                empty_left_plot = (i == 0) or (flowerbed[i - 1] == 0)
                print(empty_left_plot)
                empty_right_lot = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
                print(empty_right_lot)
                # If both plots are empty, we can plant a flower here.
                if empty_left_plot and empty_right_lot:
                    flowerbed[i] = 1
                    count += 1
                    if count >= n:
                        return True
        return count >= n

'''
Iterate through the flowerbed.

For each empty plot (flowerbed[i] == 0), check if its neighbors are also empty.

Use boundary checks for the first and last plots (i == 0 and i == len(flowerbed) - 1).

If both neighbors are empty, "plant" a flower by setting flowerbed[i] = 1 and increment the count.

If count reaches n, return True early.

Complexity:

Time: O(L), where L is the length of the flowerbed, as you only make one pass.

Space: O(1), as you only use a few variables for counting and indexing. You are modifying the input array in-place, which is a constant space operation.'''