class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        max_water = 0

        while left < right:
            height_left = height[left]
            height_right = height[right]
            width = right - left
            current_water = min(height_left, height_right)*width
            max_water = max(max_water, current_water)

            if height_left < height_right:
                left += 1
            else:
                right -=1

        return max_water
