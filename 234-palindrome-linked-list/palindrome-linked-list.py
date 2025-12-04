# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        sec = slow.next
        prev = slow.next = None
        while sec:
            temp = sec.next
            sec.next = prev
            prev = sec
            sec = temp
        
        sec = prev 
        first = head 
        while sec:
            if first.val == sec.val:
                sec = sec.next
                first = first.next
            else:
                return False
        return True

        
