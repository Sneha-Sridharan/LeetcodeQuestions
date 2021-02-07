class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode map[] = new ListNode[30];
        int i=0;
        ListNode temp = head;
        while(temp!=null)
        {
            map[i]=temp;
            i+=1;
            temp=temp.next;
        }
        if(n-1>i)
            return head;
        if(i-n==0)
            return head.next;
        map[i-n-1].next=map[i-n].next;
        return head;
    }
}