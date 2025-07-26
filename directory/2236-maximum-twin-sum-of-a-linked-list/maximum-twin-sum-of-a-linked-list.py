# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        prev_slow = None
        slow = head
        fast = head

        while fast and fast.next:
            prev_slow = slow
            slow = slow.next
            fast = fast.next.next

        if prev_slow:
            prev_slow.next = None  # Break the link between the first and second halves of the list

        reversed_second_half_head = None
        current = slow

        while current:
            next_node = current.next
            current.next = reversed_second_half_head
            reversed_second_half_head = current
            current = next_node

        max_twin_sum = 0

        ptr1 = head
        ptr2 = reversed_second_half_head

        while ptr1 and ptr2:
            current_sum = ptr1.val + ptr2.val
            max_twin_sum = max(max_twin_sum, current_sum)

            ptr1 = ptr1.next
            ptr2 = ptr2.next

        return max_twin_sum

        # Initialize pointers for finding the middle and for breaking the list


# prev_slow will track the node just before 'slow'
# slow and fast pointers start at the head
# Move fast pointer twice as fast as slow pointer
# Update prev_slow to keep track of the node before 'slow'
# When the loop finishes, 'slow' will be at the start of the second half
# and 'prev_slow' will be the last node of the first half.

# Break the link between the first and second halves of the list
# Initialize variables for reversing the second half of the list
# 'reversed_second_half_head' will become the new head of the reversed part
# Iterate through the second half
# Store the next node before modifying the current node's pointer
# Reverse the current node's pointer to point to the previously processed node
# Move 'reversed_second_half_head' to the current node
# Move to the next node in the original second half


# Initialize a variable to store the maximum twin sum found
# Set up pointers for the first half (original head) and the reversed second half
# Iterate while both pointers are valid (they will run out at the same time)
# Calculate the sum of the values of the current twin pair
# Update the maximum twin sum if the current sum is greater
# Move both pointers to their next nodes
# Return the maximum twin sum found
