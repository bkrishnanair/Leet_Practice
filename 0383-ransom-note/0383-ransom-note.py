from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Count frequency of each character in magazine
        magazine_count = Counter(magazine)

        # Check if ransomNote can be formed
        for char in ransomNote:
            if magazine_count[char] == 0:
                return False  # Not enough characters
            magazine_count[char] -= 1  # Use one occurrence of the character

        return True  # Successfully built ransomNote

        #Since all characters were successfully used, the function returns True.
