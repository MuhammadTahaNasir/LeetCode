class Solution {
public:
    bool checkIfPangram(string sentence) {
        vector<bool> alpha(26, false);

        for (char ch : sentence) {
            if (ch >= 'a' && ch <= 'z') {
                alpha[ch - 'a'] = true;
            }
        }

        for (bool present : alpha) {
            if (!present) {
                return false;
            }
        }

        return true;
    }
};
