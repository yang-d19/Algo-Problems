
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* ans = new ListNode();
        ListNode* head = ans;

        int digit = 0;
        int carry = 0;
        while (l1 != nullptr or l2 != nullptr) {
            int val1 = 0;
            int val2 = 0;
            if (l1 != nullptr) {
                val1 = l1->val;
            }
            if (l2 != nullptr) {
                val2 = l2->val;
            }
            digit = (val1 + val2 + carry) % 10;
            carry = (val1 + val2 + carry) / 10;
            head->next = new ListNode(digit);
            head = head->next;
        }
        return ans->next;
    }
};

int main(void) {
    Solution sol;
    
    return 0;
}