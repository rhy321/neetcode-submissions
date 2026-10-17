# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        arr = []
        ptr = head

        while ptr:
            arr.append(ptr)
            ptr = ptr.next

        if not arr: return

        i, j = 0, len(arr) - 1

        while i < j:
            arr[i].next = arr[j]
            i += 1
            if i < j:
                arr[j].next = arr[i]
                j -= 1

        arr[j].next = None

        # pt = arr[0]

        # while pt:
        #     print(pt.val)
        #     pt = pt.next