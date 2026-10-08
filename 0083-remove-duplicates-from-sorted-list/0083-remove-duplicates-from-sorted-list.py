# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        # Handle the empty list edge case
        if not head:
            return None
            
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                # Skip the duplicate node by changing the pointer
                curr.next = curr.next.next
            else:
                curr = curr.next
        return  head

