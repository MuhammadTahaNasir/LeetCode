class Solution {
public:
    string defangIPaddr(string address) {
        string defangedAddress;
        defangedAddress.reserve(address.size() + 6); // Pre-allocate memory

        for (char c : address) {
            if (c == '.') {
                defangedAddress += "[.]";
            } else {
                defangedAddress += c;
            }
        }

        return defangedAddress;
    }
};
