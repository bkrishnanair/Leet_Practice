class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        result = []

        for i in range(len(words) - 1, -1, -1):
            result.append(words[i])
            if i != 0:
                result.append(" ")

        return "".join(result)


# words = s.split() return " ".join(words[::-1])  -- splits a string into a list of substrings based on a specified delimiter.

# This loop iterates through the indices of the words list from the last index (len(words) - 1) to the first index (0), in reverse order. The range() function generates the indices.
# Inside the loop, each word words[i] is appended to the res list. If the current index i is not 0, a space character " " is also appended to the list. This ensures that words are separated by a space in the final reversed string, except after the last word.

# Overall, this code reverses the order of words in the input string s and stores them in the res list, with spaces in between the words.