#include <iostream>

class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0) {
            return false;
        }
        long long tmp_x = x;
        long long y = 0;
        while (tmp_x > 0) {
            y = y * 10 + tmp_x % 10;
            tmp_x /= 10;
        }
        return ((long long)x == y);
    }
};

int main(void) {
    Solution sol;
    while (true) {
        int x;
        std::cin >> x;
        bool res = sol.isPalindrome(x);
        std::cout << res << std::endl;
    }
    
    return 0;
}