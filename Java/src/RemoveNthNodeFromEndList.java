public class RemoveNthNodeFromEndList {
    /**
     * Definition for singly-linked list.
     * public class ListNode {
     *     int val;
     *     ListNode next;
     *     ListNode() {}
     *     ListNode(int val) { this.val = val; }
     *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
     * }
     */

    // Problem Statement: Given the head of a linked list, remove the nth node from the end of the list and return its head.

    class Solution {
        public ListNode removeNthFromEnd(ListNode head, int n) {
            int listLen = 0;
            ListNode firstNode = head;
            while(head != null){
                listLen ++;
                head = head.next;
            }
            if(listLen == 1 && n == 1){return null;}
            if(listLen == n){return firstNode.next;}

            head = firstNode;
            for(int i = 0; i < listLen-n-1; i++){
                head = head.next;
            }
            if(head.next == null){head.next = null;}
            else{head.next = (head.next).next;}
            return firstNode;
        }
    }
}
