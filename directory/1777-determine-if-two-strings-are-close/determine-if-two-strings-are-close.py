class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Condition 1: Strings must be of the same length.
        if len(word1) != len(word2):
            return False

 # Use Counter to get the frequency of each character.
        freq1 = Counter(word1)
        freq2 = Counter(word2)
 # Condition 2: The set of unique characters must be the same.
        # We can check this by comparing the keys of the Counter objects.
        if freq1.keys() != freq2.keys():
            return False
   # Condition 3: The sorted lists of frequencies must be identical.
        # This checks if the "frequency signature" is the same.
        if sorted(freq1.values()) != sorted(freq2.values()):
            return False
            
        # If all conditions pass, the strings are close.
        return True


'''
IGNORE the operations as they dont change anything, they are asking just to see if they are close, we dont need to make them close,. if the above checks are tur that means we can perform opertaions to make them close

'''