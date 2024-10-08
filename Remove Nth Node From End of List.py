# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = ListNode(0, head)
        prev = node
        fast = head

        while n > 0:
            fast = fast.next
            n -= 1
        
        while fast:
            fast = fast.next
            prev = prev.next
        prev.next = prev.next.next
        return node.next
        
