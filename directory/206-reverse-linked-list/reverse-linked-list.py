# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None       # Pointer to the previous node (initially None)
        current = head    # Pointer to the current node (starts at the head)

        # Iterate through the list
        while current:
            # 1. Store the next node before modifying current.next
            next_node = current.next
            
            # 2. Reverse the current node's pointer to point to the previous node
            current.next = prev
            
            # 3. Move the pointers one step forward for the next iteration
            prev = current      # The current node becomes the previous node for the next step
            current = next_node # Move to the next node in the original list
            
        # After the loop, 'prev' will be the new head of the reversed list
        return prev
        

'''
recursion - X

Sure, I can explain the problem "206. Reverse Linked List" and its iterative and recursive solutions in a detailed yet concise manner, as you've requested for all problems.

This is a **classic interview problem** that tests your understanding of linked lists and pointer manipulation. It has two primary solutions: an **iterative** approach (using pointers) and a **recursive** approach. While both are valid, the iterative solution is generally preferred in interviews due to its **O(1) space complexity** compared to the recursive solution's **O(N) space complexity** (due to the call stack).

-----

## 1\. Iterative Solution (Using 3 Pointers)

This method involves traversing the linked list and, for each node, changing its `next` pointer to point to the previous node instead of the subsequent one. To do this safely without losing track of the list, we use three pointers.

### The Logic \U0001f9e0

Imagine you're re-linking a train's carriages backward. For each carriage (`current`), you need to know which carriage came **before** it (`prev`) so you can link it there, and which carriage comes **after** it (`next_node`) so you can move to it next.

1.  **Initialization:**

      * `prev`: Starts as `None`. This pointer will keep track of the node that was just processed and whose `next` pointer has been reversed. Initially, there's no node before the `head`.
      * `current`: Starts as `head`. This pointer iterates through the original list, representing the node we are currently processing.

2.  **Iteration (Loop):** We loop as long as `current` is not `None` (meaning we haven't reached the end of the original list).

      * **Step 1: Save `next_node`**: Before we change `current.next`, we need to store a reference to the node that originally came *after* `current`. This is crucial to avoid losing the rest of the list. So, `next_node = current.next`.
      * **Step 2: Reverse `current.next`**: Now, we reverse the pointer of the `current` node. Instead of pointing to `next_node`, it should now point to `prev`. So, `current.next = prev`.
      * **Step 3: Advance Pointers**: We've processed `current`, so we need to move `prev` and `current` forward for the next iteration:
          * `prev` becomes `current` (the node we just processed, which is now the "previous" for the next iteration).
          * `current` becomes `next_node` (the node we saved earlier, which is the next node to process).

3.  **Return Value:** Once the loop finishes, `current` will be `None`, meaning we've iterated through the entire original list. At this point, `prev` will be pointing to the last node of the original list, which is now the **new head** of the reversed list.

### The Code \U0001f4bb

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None       # Pointer to the previous node (initially None)
        current = head    # Pointer to the current node (starts at the head)

        # Iterate through the list
        while current:
            # 1. Store the next node before modifying current.next
            next_node = current.next
            
            # 2. Reverse the current node's pointer to point to the previous node
            current.next = prev
            
            # 3. Move the pointers one step forward for the next iteration
            prev = current      # The current node becomes the previous node for the next step
            current = next_node # Move to the next node in the original list
            
        # After the loop, 'prev' will be the new head of the reversed list
        return prev
```

-----

## 2\. Recursive Solution

The recursive approach elegantly breaks down the problem into smaller, similar sub-problems. The core idea is to reverse the "rest" of the list and then correctly attach the current `head` to the end of that reversed "rest."

### The Logic \U0001f9e0

Think of it this way: to reverse `[1, 2, 3, 4, 5]`:

1.  Recursively reverse `[2, 3, 4, 5]` to get `[5, 4, 3, 2]`.

2.  Now you have `1` and `[5, 4, 3, 2]`. You need to connect `2` (which is now `head.next`) to `1`.

3.  The final result will be `[5, 4, 3, 2, 1]`.

4.  **Base Case:**

      * If the list is empty (`head is None`) or has only one node (`head.next is None`), it's already reversed. In this scenario, we simply return `head`. This is crucial to stop the recursion.

5.  **Recursive Step:**

      * Call `self.reverseList(head.next)`. This is the magical part. It assumes that the function will correctly reverse the sub-list starting from `head.next`. The return value, `new_head`, will be the **head of this fully reversed sub-list** (which was the original tail).
      * Now, we have:
          * `head`: The current node we're processing (e.g., `1` in `[1, 2, 3, 4, 5]`).
          * `head.next`: The node *after* `head` in the original list (e.g., `2`). After the recursive call, `head.next` still points to `2`, but `2` is now the last element of the reversed sub-list.
          * `new_head`: The head of the fully reversed sub-list (e.g., `5` from `[5, 4, 3, 2]`).

6.  **Relinking Pointers:** This is the crucial step where the current node is integrated into the reversed sub-list.

      * `head.next.next = head`: This is the key. The node that was originally *after* `head` (i.e., `head.next`, which is now `2`) should have its `next` pointer point back to `head` (i.e., `1`). So, `2`'s `next` pointer now points to `1`. This links `2 -> 1`.
      * `head.next = None`: The current `head` (e.g., `1`) is now the *last* node in the newly formed reversed list segment. Therefore, its `next` pointer should be set to `None`.

7.  **Return Value:** The `new_head` (e.g., `5`) that was returned from the deepest recursive call is the true head of the **entirely reversed list**. Each recursive call will return this same `new_head` all the way up the call stack.

### The Code \U0001f4bb

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1. Base Case: If the list is empty or has only one node, it's already reversed.
        if not head or not head.next:
            return head

        # 2. Recursively reverse the rest of the list.
        # 'new_head' will be the head of the completely reversed sub-list (original tail).
        new_head = self.reverseList(head.next)

        # 3. Relink pointers for the current node:
        # The node that was originally 'head.next' (e.g., node '2' for '1->2->3')
        # is now the last node of the reversed sub-list (e.g., '2' in '5->4->3->2').
        # Make its 'next' pointer point back to the current 'head' (e.g., '1').
        head.next.next = head
        
        # Make the current 'head' the new tail of this segment.
        # Its 'next' pointer should be None.
        head.next = None

        # 4. Return the overall new head (which remains the same throughout the recursion).
        return new_head
```

'''