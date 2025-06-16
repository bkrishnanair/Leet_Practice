class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        #Create Dict to store character freq
        char_count = {}

        for char in s:
            char_count[char] = char_count.get(char,0)+1
        for char in t:
            if char not in char_count or char_count[char] == 0:
                return False
            char_count[char] -= 1

        return True



    
# Explanation:

# First, we check if the lengths of the two strings are different. If they are, then they cannot be anagrams, so we return False.
# We create a dictionary char_count to store the frequency of each character in the first string s.
# We iterate through the first string s and increment the count of each character in the char_count dictionary.
# We then iterate through the second string t and decrement the count of each character in the char_count dictionary. If a character in t is not found in char_count or its count is already 0, we return False because the strings are not anagrams.
# If we successfully iterate through both strings and the char_count dictionary is empty (all counts are 0), we return True because the strings are anagrams.
# The time complexity of this solution is O(n), where n is the length of the input strings, as we iterate through both strings once. The space complexity is also O(n) due to the use of the char_count dictionary.