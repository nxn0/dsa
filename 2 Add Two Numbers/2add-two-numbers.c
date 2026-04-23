/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode dum; 
    struct ListNode *ptr = &dum;
    int c = 0;
    while (l1 || l2 || c){
        int sum = (l1 ? l1->val :0) + (l2 ? l2->val :0) +c;
        c=sum/10;
        ptr->next=(struct ListNode*)malloc(sizeof(struct ListNode));
        ptr = ptr->next;
        ptr->val = sum%10;
        ptr->next = NULL;

        if (l1) l1=l1->next;
        if (l2) l2=l2->next;
    }
    return dum.next;
}