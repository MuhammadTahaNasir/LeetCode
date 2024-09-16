class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if (!head || !head->next || k == 0) {
            return head;  // Return head if list is empty, single node, or no rotation needed
        }

        // Step 1: Count the number of nodes
        int count = 1;
        ListNode* temp = head;
        while (temp->next != nullptr) {
            count++;
            temp = temp->next;
        }

        // Step 2: Connect the last node to the head to form a circular linked list
        temp->next = head;

        // Step 3: Calculate effective rotations
        k = k % count;

        // Step 4: Find the new tail, which is (count - k) steps from the current head
        ListNode* curr = head;
        for (int i = 1; i < count - k; i++) {
            curr = curr->next;
        }

        // Step 5: The new head is the node after the new tail
        ListNode* newHead = curr->next;

        // Step 6: Break the circular link
        curr->next = nullptr;

        return newHead;
    }
};