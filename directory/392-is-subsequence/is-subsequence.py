class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j =0, 0

        while i<len(s) and j<len(t):
            if s[i]==t[j]:
                i+=1
            j+=1
        return i == len(s) #returns true or false

#iterate through two string two diff pointers compare if the elements are equal  if number of elements are equal to the length of the subsequent string then it is.

            