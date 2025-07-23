class Solution:
    def decodeString(self, s: str) -> str:
        # The stack will store tuples of (previous_string, repeat_count)
        stack = []
        current_num = 0
        current_string = ""

        for char in s:
            # If the character is a digit, build the number.
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            
            # If it's an opening bracket, save the current state and reset.
            elif char == '[':
                stack.append((current_string, current_num))
                current_string = ""
                current_num = 0
            
            # If it's a closing bracket, decode.
            elif char == ']':
                # Pop the last saved string and its repeat count.
                prev_string, repeat_count = stack.pop()
                
                # The new current_string is the previous one plus the
                # repeated version of the string we just finished building.
                current_string = prev_string + current_string * repeat_count
            
            # If it's a letter, append it to the current string.
            else:
                current_string += char
                
        return current_string

'''
Of course! Let's walk through the code step-by-step with the example s = "3[a2[c]]". This will make it much clearer how the stack helps us handle the nested parts.

Think of it like this: current_string is the piece of the puzzle you are currently building. The stack is where you put aside puzzle pieces that are already connected, so you can work on a new, smaller section.

## The Setup
Before the loop starts, we have three variables:

stack = [] (An empty list to store our saved work)

current_num = 0

current_string = ""

## Let's Trace the Code
We will now go through the string 3[a2[c]] one character at a time.

1. char = '3'
The code sees that '3' is a digit.

It updates current_num to 3.

State: current_num = 3, current_string = "", stack = []

2. char = '['
This is the "save your work" signal! We are about to start a new section.

We push our current work (current_string, current_num) onto the stack. Right now, that's ("", 3).

We reset current_string and current_num to start fresh for the inside part.

State: current_num = 0, current_string = "", stack = [ ("", 3) ]

3. char = 'a'
This is a simple letter.

We append it to our current_string.

State: current_num = 0, current_string = "a", stack = [ ("", 3) ]

4. char = '2'
Another digit.

We update current_num to 2.

State: current_num = 2, current_string = "a", stack = [ ("", 3) ]

5. char = '['
Another "save your work" signal! We're going one level deeper.

We push our current work ("a", 2) onto the stack.

We reset again for the innermost part.

State: current_num = 0, current_string = "", stack = [ ("", 3), ("a", 2) ]

6. char = 'c'
A simple letter.

We append it to the innermost current_string.

State: current_num = 0, current_string = "c", stack = [ ("", 3), ("a", 2) ]

7. char = ']' (The first closing bracket)
This is the "finish a section" signal!

We pop from the stack to get our last saved work: ("a", 2).

So, prev_string becomes "a" and repeat_count becomes 2.

We update current_string using the formula: current_string = prev_string + current_string * repeat_count.

This becomes: current_string = "a" + "c" * 2  ➡️  "a" + "cc"  ➡️  "acc".

State: current_num = 0, current_string = "acc", stack = [ ("", 3) ]

8. char = ']' (The second closing bracket)
Another "finish a section" signal! This one is for the outermost part.

We pop from the stack again: ("", 3).

So, prev_string becomes "" and repeat_count becomes 3.

We update current_string with the same formula: current_string = prev_string + current_string * repeat_count.

This becomes: current_string = "" + "acc" * 3  ➡️  "" + "accaccacc"  ➡️  "accaccacc".

State: current_num = 0, current_string = "accaccacc", stack = []

## The Final Result
The loop has now finished. The function returns the final value of current_string, which is "accaccacc".
'''