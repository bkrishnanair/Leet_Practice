class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        i = 0
        while i < len(word1) or i < len(word2):
            if i < len(word1):
                merged.append(word1[i])
            if i < len(word2):
                merged.append(word2[i])
            i += 1
        return ''.join(merged)


#We use a single index i and iterate while either string still has characters left. At each step, we append the character from word1 if available, then the character from word2 if available. The boundary checks handle strings of different lengths. We store characters in a list because string concatenation is expensive in Python, and finally use ''.join() to build the result. The time complexity is O(m+n) and the space complexity is O(m+n).