class Solution:
    def compress(self, chars: List[str]) -> int:
        if not chars:
            return 0

        write = 1
        prev_char = chars[0]
        count = 1

        for char in chars[1:]:
            if char == prev_char:
                count += 1
            else:
                if count > 1:
                    for digit in str(count):
                        chars[write] = digit
                        write += 1
                chars[write] = char
                write += 1
                prev_char = char
                count = 1

        if count > 1:
            for digit in str(count):
                chars[write] = digit
                write += 1

        return write

#Iterate through input array chars.
# For each group of consecutive repeating characters:
# Write the character to the array at current position write.
# If the count is greater than 1, write the count to the array at the next position, incrementing write by the length of the count.
# Increment write by 1.
# Return new length of array (write).