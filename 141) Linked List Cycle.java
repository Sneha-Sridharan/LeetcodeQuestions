/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        ListNode slow=head;
        ListNode fast=null;
        if(head == null || head.next==null){
            return false;
        }
        
        if(head.next!=null){
            fast=head.next.next; 
        }
       
        while(slow!=null && fast !=null && fast.next!=null){
            if(slow==fast){
                return true;
            }
            else{
                slow=slow.next;
                fast=fast.next.next;
            }
        }
        return false;
        
    // Alternate solution
    //     ListNode temp=new ListNode();
    //     ListNode nextnode;
    //     if(head==null){
    //         return false;
    //     }
    //     while(head.next!=null){
    //         nextnode=head.next;
    //         head.next=temp;
    //         if(nextnode==temp){
    //             return true;
    //         }
    //         else{
    //             head=nextnode;
    //         }
    //     }
    //     return false;
     }
}