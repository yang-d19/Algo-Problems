#include <iostream>
#include <vector>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

void append(ListNode* head, vector<int>& arr) {
    while (head->next != nullptr) {
        head = head->next;
    }
    for (auto ele: arr) {
        head->next = new ListNode(ele);
        head = head->next;
    }
}

void append(ListNode* head, int ele) {
    while (head->next != nullptr) {
        head = head->next;
    }
    head->next = new ListNode(ele);
}

void delFromEnd(ListNode* head) {
    while (head->next != nullptr && head->next->next != nullptr) {
        head = head->next;
    }
    if (head->next == nullptr) {
        return ;
    }
    else {
        head->next = head->next->next;
    }
}

void display(ListNode* head) {
    if (head == nullptr) {
        return ;
    }
    while (head->next != nullptr) {
        cout << head->val << " ";
        head = head->next;
    }
    if (head != nullptr) {
        cout << head->val << " ";
    }
    cout << endl;
}

ListNode* create(vector<int>& arr) {
    ListNode* head = new ListNode();
    append(head, arr);
    return head;
}

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
                l1 = l1->next;
            }
                
            if (l2 != nullptr) {
                val2 = l2->val;
                l2 = l2->next;
            }
        
            digit = (val1 + val2 + carry) % 10;
            carry = (val1 + val2 + carry) / 10;
            head->next = new ListNode(digit);
            head = head->next;
        }
        if (carry == 1) {
            head->next = new ListNode(1);
        }
        return ans->next;
    }
};

int main(void) {
    Solution sol;
    vector<int> v1 = {2, 4, 3};
    vector<int> v2 = {5, 6, 4};
    ListNode* l1 = create(v1);
    ListNode* l2 = create(v2);
    ListNode* result = sol.addTwoNumbers(l1, l2);
    display(result);
    return 0;
}