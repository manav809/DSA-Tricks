# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        head = dummy
        p = list1
        q = list2

        while p and q:
            if p.val < q.val:
                dummy.next = p
                p = p.next
            elif p.val >= q.val:
                dummy.next = q
                q = q.next
            dummy = dummy.next
        if p:
            dummy.next = p
        if q:
            dummy.next = q
        return head.next
