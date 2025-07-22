class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []

        for new in asteroids:
            # This loop correctly handles collisions
            while stack and new < 0 and stack[-1] > 0:
                # Case 1: New asteroid is bigger, stack top explodes.
                if abs(new) > abs(stack[-1]):
                    stack.pop()
                    continue  # The new asteroid continues to the next on the stack

                # Case 2: Both are same size, both explode.
                elif abs(new) == abs(stack[-1]):
                    stack.pop()
                    break # new asteroid also explodes, so break
                
                # Case 3 : New asteroid is smaller, it explodes.
                else: 
                    break # new asteroid explodes, so break

            else:
                # This 'else' only runs if the 'while' loop did NOT break.
                # It means the new asteroid survived all collisions.
                stack.append(new)
                
        return stack