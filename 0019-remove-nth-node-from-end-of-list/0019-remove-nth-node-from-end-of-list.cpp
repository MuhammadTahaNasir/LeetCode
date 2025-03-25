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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        // Step 1: Count the number of nodes
        int count = 0;
        ListNode* temp = head;
        while (temp != nullptr) {
            count++;
            temp = temp->next;
        }

        // Step 2: Find the node to remove (count - n from start)
        count -= n;

        // Step 3: Special case: removing the head
        if (count == 0) {
            temp = head;
            head = head->next;
            delete temp;
            return head;
        }

        // Step 4: Traverse the list to find the node to remove
        ListNode* curr = head;
        ListNode* prev = nullptr;
        while (count--) {
            prev = curr;
            curr = curr->next;
        }

        // Step 5: Remove the nth node from the end
        prev->next = curr->next;
        delete curr;

        return head;  // Ensure head is always returned
    }
};