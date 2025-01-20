class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiouAEIOU")  # Set of vowel characters
        max_vowel_count = 0
        current_vowel_count = 0
        
        # Calculate the number of vowels in the first 'k' characters
        for i in range(min(k, len(s))):  # Ensure we don't exceed string length
            if s[i] in vowels:
                current_vowel_count += 1
        
        max_vowel_count = current_vowel_count

        # Use a sliding window to check the next characters
        for i in range(k, len(s)):
            # Remove the character that is sliding out of the window
            if s[i - k] in vowels:
                current_vowel_count -= 1
            # Add the new character that is sliding into the window
            if s[i] in vowels:
                current_vowel_count += 1
            
            # Update max if current window has more vowels
            max_vowel_count = max(max_vowel_count, current_vowel_count)

        return max_vowel_count

