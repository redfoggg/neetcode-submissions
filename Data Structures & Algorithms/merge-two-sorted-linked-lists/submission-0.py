# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        hd1, hd2 = list1, list2
        while hd1 and hd2:
            tmp = None
            if hd1.val > hd2.val:
                tmp = hd2.next
                hd2.next = hd1
                hd2 = tmp
            else:
                tmp = hd1.next
                hd1.next = hd2
                hd1 = tmp

        return list1 if list1 else list2


        