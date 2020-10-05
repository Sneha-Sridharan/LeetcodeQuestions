class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        last=head=None
        while l1 and l2:
            if l1.val<=l2.val and last:
                last.next=ListNode(l1.val)
                l1=l1.next
                last=last.next
            elif l2.val<=l1.val and last:
                last.next=ListNode(l2.val)
                l2=l2.next
                last=last.next
            elif l1.val<=l2.val:
                head=last=ListNode(l1.val)
                l1=l1.next
            else:
                head=last=ListNode(l2.val)
                l2=l2.next
        if l1!=None:
            if last==None:
                head=l1
            else:
                last.next=l1
        if l2!=None:
            if last==None:
                head=l2
            else:
                last.next=l2
        return head
                    
