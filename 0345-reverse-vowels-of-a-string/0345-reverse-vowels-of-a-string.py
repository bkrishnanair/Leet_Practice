class Solution:
    def reverseVowels(self, s: str) -> str:
        # Vowels for quick O(1) lookup.
        vowels = set("aeiouAEIOU")

        # Strings are immutable, so convert to a list.
        chars = list(s)

        left = 0
        right = len(chars) - 1

        while left < right: 

            # Move left pointer until it finds a vowel.
            while left < right and chars[left] not in vowels:
                left += 1

            # Move right pointer until it finds a vowel.
            while left < right and chars[right] not in vowels:
                right -= 1

            # Swap the vowels.  (is this 2 pointer?)
            chars[left], chars[right] = chars[right], chars[left]

            # Move both pointers inward.
            left += 1
            right -= 1

        return ''.join(chars)

#I use two pointers, one starting from the left and one from the right. Each pointer skips non-vowel characters until it finds a vowel. Then I swap the vowels and continue moving inward. This reverses the order of the vowels while keeping all other characters in their original positions. The algorithm runs in O(n) time and uses O(n) space due to converting the string into a mutable list.

#We use while instead of for because the movement of left and right is dynamic. Each pointer may advance a different number of steps depending on where the next vowel is found. Since we don't know the number of iterations in advance and the loop stops when left >= right, a while loop is more appropriate than a for loop.