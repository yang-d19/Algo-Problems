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

void append(ListNode* head, vector<int> arr) {
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

void display(ListNode* head) {
    while (head->next != nullptr) {
        cout << head->val << " ";
        head = head->next;
    }
    if (head != nullptr) {
        cout << head->val << " ";
    }
    cout << endl;
}

int main(void) {
    
    return 0;
}