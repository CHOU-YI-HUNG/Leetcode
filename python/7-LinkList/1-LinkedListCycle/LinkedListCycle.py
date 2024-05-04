# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        a=b=head                                
        while a!=None and b!=None and b.next!=None:
            a=a.next
            b=(b.next).next
            if a==b: return True
                
        return False