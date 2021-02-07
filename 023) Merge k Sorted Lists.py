class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        l=[]
        for count in lists:
            while count:
                l.append(count.val)
                count=count.next
        l.sort()
        temp=head=ListNode()
        for elem in l:
            temp.next=ListNode(elem)
            temp=temp.next
        return head.next