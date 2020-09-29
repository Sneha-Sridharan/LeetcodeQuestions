# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        result=l1
        head1=l1
        head2=l2
        carry=0
        prev=None
        while head1 and head2:
            head1.val+=head2.val+carry
            carry=0
            if head1.val>9:
                carry=head1.val//10
                head1.val%=10
            prev=head1
            head1=head1.next
            head2=head2.next
        
        if not head1 and not head2:
            if carry!=0:
                prev.next=ListNode(carry)
        while head1:
            head1.val+=carry
            carry=0
            carry=head1.val//10
            head1.val%=10
            prev=head1
            head1=head1.next
        while head2:
            prev.next=head2
            head2.val+=carry
            carry=0
            carry=head2.val//10
            head2.val%=10
            prev=head2
            head2=head2.next
        if carry!=0:
            prev.next=ListNode(carry)
            
            
        return result
        
