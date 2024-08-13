# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        odd = head
        even = odd.next
        even_head = even
        while even and even.next:
            odd.next, odd = even.next, even.next
            even.next, even = odd.next, odd.next
        

        odd.next = even_head
        
        return head
