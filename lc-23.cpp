#include <vector>
using namespace std;


struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        int len = lists.size();
        ListNode* currNodes[len];
        ListNode* result = new ListNode();
        ListNode* head = result;

        int minVal = INT_MAX;
        for (int idx = 0; idx < len; idx++) {
            currNodes[idx] = lists[idx];
            minVal = min(minVal, currNodes[idx]->val);
        }

        int reachEndCnt = 0;

        while (reachEndCnt < len) {
            int nextMinVal = INT_MAX;

            for (int idx = 0; idx < len; idx++) {
                while (currNodes[idx] != nullptr && currNodes[idx]->val <= minVal) {
                    head->next = new ListNode(currNodes[idx]->val);
                    head = head->next;
                    currNodes[idx] = currNodes[idx]->next;
                }

                if (currNodes[idx] != nullptr) {
                    nextMinVal = min(nextMinVal, currNodes[idx]->val);
                }
                else {
                    reachEndCnt++;
                }
            }
            minVal = nextMinVal;
        }
        return result->next;
    }
};