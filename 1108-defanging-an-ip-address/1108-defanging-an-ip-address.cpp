class Solution {
public:
    string defangIPaddr(string address) {
        string result;
        result.reserve(address.size() + 6); // Pre-allocate memory for the final string
        for (char c : address) {
            if (c == '.') {
                result += "[.]";
            } else {
                result += c;
            }
        }
        return result;
    }
};