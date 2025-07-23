# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next or not head.next.next:
            return head

        odd_ptr = head  # Pointer for the current end of the odd-indexed list
        even_ptr = head.next  # Pointer for the current end of the even-indexed list
        even_head = head.next # Store the head of the even-indexed list for later connection

        while even_ptr and even_ptr.next:

            odd_ptr.next = even_ptr.next
            # Move odd_ptr forward to the newly linked odd node
            odd_ptr = odd_ptr.next

            even_ptr.next = odd_ptr.next
            # Move even_ptr forward to the newly linked even node
            even_ptr = even_ptr.next

        odd_ptr.next = even_head

        # Return the head of the modified list (which is the original head)
        return head


# Handle edge cases: empty list, single node, or two nodes.
# No rearrangement is needed for these cases.
# Initialize pointers for odd and even lists

# Iterate through the list, separating odd and even nodes
# The loop continues as long as there are at least two more nodes to process
# (one odd, one even)

# Connect current odd_ptr to the next odd node
# The next odd node is currently even_ptr.next


# Connect current even_ptr to the next even node
# The next even node is currently odd_ptr.next


# After the loop, odd_ptr is at the last node of the odd-indexed list.
# Connect the tail of the odd list to the head of the even list.
