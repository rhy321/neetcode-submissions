# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = list1
        ptr2 = list2

        if not ptr1 and ptr2: return ptr2
        if not ptr2 and ptr1: return ptr1

        curr = None
        prev = None
        head = None

        while ptr1 and ptr2:

            if ptr2.val <= ptr1.val:
                curr = ptr2
                ptr2 = ptr2.next
            else:
                curr = ptr1
                ptr1 = ptr1.next

            if prev:
                prev.next = curr
            else:
                head = curr

            prev = curr


        if ptr1:
            prev.next = ptr1

        elif ptr2:
            prev.next = ptr2

        return head