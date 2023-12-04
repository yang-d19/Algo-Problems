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

int main(void) {
    vector<int> v1 = {1, 3, 2, 9, 7, 12, -4, 6};
    ListNode* list1 = create(v1);
    display(list1->next);
    delFromEnd(list1);
    delFromEnd(list1);
    display(list1->next);
    return 0;
}