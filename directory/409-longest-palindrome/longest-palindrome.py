class Solution:
    def longestPalindrome(self, s: str) -> int:
        # Create a dictionary to store the frequency of each character
        char_freq = {}
        for char in s:
            char_freq[char] = char_freq.get(char, 0) + 1
        
        # Initialize the length of the longest palindrome
        longest_palindrome = 0
        
        # Check the frequencies of the characters
        has_odd_char = False
        for freq in char_freq.values():
            if freq % 2 == 0:
                longest_palindrome += freq
            else:
                longest_palindrome += freq - 1
                has_odd_char = True
        
        # If there is at least one character with odd frequency, add 1 to the length
        if has_odd_char:
            longest_palindrome += 1
        
        return longest_palindrome