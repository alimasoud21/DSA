# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        pt1, pt2 = head, head.next
        while pt2:
            if pt1.val == pt2.val:
                pt2 = pt2.next
                pt1.next = pt2
            else:
                pt1 = pt2
                pt2 = pt2.next
        return head