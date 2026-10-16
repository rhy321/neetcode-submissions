# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = list1
        ptr2 = list2

        curr = None
        prev = None
        head = None

        if ptr1 == None and ptr2: return ptr2
        if ptr2 == None and ptr1: return ptr1

        while ptr1 and ptr2:

            if ptr2.val <= ptr1.val:
                curr = ptr2
                ptr2 = ptr2.next
            else:
                curr = ptr1
                ptr1 = ptr1.next

            if prev != None:
                prev.next = curr
            else:
                head = curr

            prev = curr


        if ptr1 and prev:
            prev.next = ptr1

        elif ptr2 and prev:
            prev.next = ptr2

        return head