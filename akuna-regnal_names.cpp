// https://www.1point3acres.com/bbs/thread-1009323-1-1.html
// problem 2

#include <string>
#include <vector>

// std::vector<std::string> sortRegnalNames(const std::vector<std::string> &names) {
//     for (const std::string& name: names) {

//     }
// }

#include <iostream>
#include <unordered_map>
using namespace std;

int romanToInt(string s) {
    unordered_map<char, int> romanDict{
        {'I', 1},
        {'V', 5},
        {'X', 10},
        {'L', 50},
        {'C', 100},
        {'D', 500},
        {'M', 1000}
    };

    int result = 0;
    int prevValue = 0;

    for (int i = s.length() - 1; i >= 0; i--) {
        int currValue = romanDict[s[i]];

        if (currValue < prevValue) {
            result -= currValue;
        } else {
            result += currValue;
        }

        prevValue = currValue;
    }

    return result;
}

int main() {
    string romanNumeral;
    cout << "Enter a Roman numeral: ";
    cin >> romanNumeral;

    int decimalValue = romanToInt(romanNumeral);
    cout << "Decimal value: " << decimalValue << endl;

    return 0;
}