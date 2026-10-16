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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* ptr1 = list1;
        ListNode* ptr2 = list2;

        if (ptr1 == nullptr) return ptr2;
        if (ptr2 == nullptr) return ptr1;

        ListNode* curr = nullptr;
        ListNode* head = nullptr;
        ListNode* prev = nullptr;

        while (ptr1 && ptr2){
            if (ptr2 -> val <= ptr1->val){
                curr = ptr2;
                ptr2 = ptr2->next;
            } else {
                curr = ptr1;
                ptr1 = ptr1->next;
            }

            if (prev != nullptr) {
                prev->next = curr;
            } else {
                head = curr;
            }

            prev = curr;
        }

        if (ptr1) {
            prev->next = ptr1;
        } else if (ptr2) {
            prev->next = ptr2;
        }

        return head;
    }
};
