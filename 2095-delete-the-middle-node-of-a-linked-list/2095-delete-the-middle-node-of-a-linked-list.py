# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Handle edge cases for empty or single-node lists
        if not head or not head.next:
            return None # No middle node to delete, or list becomes empty

        # Use a dummy head to simplify handling the case where the middle node
        # is the original head (though per problem definition, n >= 1)
        # and more importantly, to easily get the node *before* the middle.
        dummy_head = ListNode(0)
        dummy_head.next = head

        slow_ptr = dummy_head  # Starts one step behind, will point to node *before* middle
        fast_ptr = head        # Starts at the head, moves twice as fast

        # Move fast_ptr two steps and slow_ptr one step
        # When fast_ptr reaches the end, slow_ptr will be at the node before the middle
        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        
        # At this point, slow_ptr.next is the middle node to be deleted.
        # Bypass the middle node by linking slow_ptr to the node after the middle.
        slow_ptr.next = slow_ptr.next.next

        # Return the head of the modified list (skipping the dummy node)
        return dummy_head.next