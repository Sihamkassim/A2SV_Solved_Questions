# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None
        
        # Traverse and remove non-head nodes
        curr = head
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next  # Skip next node
            else:
                curr = curr.next            # Move forward
        
        # Handle head node removal (after all others)
        if head.val == val:
            head = head.next
        
        return head