
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = slow.next = None

        #reverse second part of list
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
            
        #merge two halves
        first, second = head, prev

        #second might have less nodes
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
            