class Solution {
public:
    bool isPalindrome(string s) {
        int start = 0, end = s.size() - 1;
        while (start < end) {
            // Move start to the next alphanumeric character
            while (start < end && !isalnum(s[start])) start++;
            // Move end to the previous alphanumeric character
            while (start < end && !isalnum(s[end])) end--;
            
            // Compare the characters and then increment/decrement
            if (tolower(s[start]) != tolower(s[end])) return false;
            start++;
            end--;
        }
        return true;
    }
};
