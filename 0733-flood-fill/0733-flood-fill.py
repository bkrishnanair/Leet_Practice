from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if not image or image[sr][sc] == color:
            return image

        original_color = image[sr][sc]
        queue = deque([(sr, sc)])
        image[sr][sc] = color

        while queue:
            i, j = queue.popleft()
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_i, new_j = i + di, j + dj
                if 0 <= new_i < len(image) and 0 <= new_j < len(image [0]) and image[new_i][new_j] == original_color:
                    image[new_i][new_j] = color
                    queue.append((new_i, new_j))

        return image



# state : change the colour of the starting pxel and other pixels with same original colour to the given colour.
#Explanation:The floodFill function first gets the dimensions of the image (m and n) and stores the starting color (start_color) of the pixel at coordinates (sr, sc).
# If the color to be filled is the same as the start_color, the function simply returns the original image.
# The dfs function is a helper function that performs the depth-first search. It takes the current coordinates (i, j) as input.
# Inside the dfs function, the base case checks if the current coordinates are out of bounds or if the current pixel has a different color than the start_color. If either of these conditions is true, the function returns without modifying the image.
# If the current pixel has the start_color, its value is updated to the color.
# The dfs function is then recursively called on the four neighboring pixels (up, down, left, right).
# After the initial call to dfs(sr, sc), the modified image is returned.
#The time complexity of this solution is O(mn), where m and n are the dimensions of the input image, as we need to visit each pixel at most once. The space complexity is O(mn) due to the recursive calls on the call stack.