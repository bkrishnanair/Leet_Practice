# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False  # No cycle if list is empty or has only one node

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next        # Move one step
            fast = fast.next.next    # Move two steps

            if slow == fast:
                return True  # Cycle detected

        return False  # No cycle found


#To determine if a linked list has a cycle, we use Floyd’s Cycle Detection Algorithm (Tortoise and Hare approach). This method efficiently detects a cycle in O(n) time using only O(1) extra space.
