/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    struct ListNode dummy;
    dummy.next = head;
    struct ListNode *fast = &dummy;
    struct ListNode *slow = &dummy;
    for(int f = 0; f < n; f++){
            fast=fast->next;
        }
    while(fast->next!=NULL){
       fast = fast->next;
       slow = slow->next; 
    }
    struct ListNode* nuke = slow->next;
    slow->next = nuke->next;
    free(nuke);
    return dummy.next;
}