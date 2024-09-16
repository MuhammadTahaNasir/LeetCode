/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode *nextNode, *prevNode, *curr;
        nextNode= nullptr, prevNode= nullptr, curr =head;
        while(curr!=nullptr){
            nextNode = curr-> next;
            curr->next = prevNode;
            prevNode = curr;
            curr = nextNode;
        }
         return prevNode;
    }

};