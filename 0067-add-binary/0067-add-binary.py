class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]

#         - Convert both binary strings to integers using int(a, 2) and int(b, 2).
# - Perform addition like normal numbers.
# - Convert the result back to binary using bin(sum)[2:].
