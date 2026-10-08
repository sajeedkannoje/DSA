# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        if not head:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        
        prev = dummy
        while prev.next and prev.next.next:
            first = prev.next
            second = first.next

            # Swap
            prev.next = second
            first.next = second.next
            second.next = first
            
            prev = first
        return dummy.next





        