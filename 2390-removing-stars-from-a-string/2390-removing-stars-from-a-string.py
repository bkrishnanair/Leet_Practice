class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for char in s:
            if char != '*':
                stack.append(char)
            else:
                stack.pop()
        return "".join(stack)

'''
Imagine you're building the result string one character at a time.

Iterate through the input string s.

If you see a normal letter, add it to the end of your result. This is like pushing onto a stack.

If you see a star (*), it means you need to delete the last letter you added. This is like popping from a stack.

After you've processed the whole input string, the characters remaining in your stack-like structure, when joined together, form the final answer.

Python Solution
A simple Python list can be used as a stack, where append() is the "push" operation and pop() is the "pop" operation.

'''