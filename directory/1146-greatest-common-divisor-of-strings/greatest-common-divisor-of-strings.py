class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # A simple helper function to calculate the GCD of two integers
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        # The core logic of the solution
        if str1 + str2 != str2 + str1:
            return ""
        
        len1, len2 = len(str1), len(str2)
        max_len = gcd(len1, len2)
        
        return str1[:max_len]