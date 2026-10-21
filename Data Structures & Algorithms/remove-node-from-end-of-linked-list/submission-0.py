# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ptr = head
        cnt = 0
        while ptr:
            cnt += 1
            ptr = ptr.next
        
        if cnt == n: return head.next

        ptr1 = head

        for i in range( cnt - n ):
            prev = ptr1
            ptr1 = ptr1.next

        prev.next = ptr1.next

        return head