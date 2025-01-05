#include <stack>
#include <string>
using namespace std;

class Solution {
public:
    int longestValidParentheses(string s) { // Change made here
        stack<int> stk;
        stk.push(-1); // Pushing -1 to handle the edge cases
        int maxLength = 0;

        for (int i = 0; i < s.length(); i++) {
            if (s[i] == '(') {
                stk.push(i); // Push the index of opening bracket
            } else {
                stk.pop(); // Popping should be done for the closing brackets

                if (stk.empty()) {
                    stk.push(i); // If we have an empty stack, push the current index
                } else {
                    // The length of the valid substring
                    maxLength = max(maxLength, i - stk.top());
                }
            }
        }

        return maxLength; // Return the maximum length
    }
};
