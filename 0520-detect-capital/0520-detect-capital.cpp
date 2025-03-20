class Solution {
public:
    bool detectCapitalUse(string word) {
        int capitals = 0;
        for (char c : word) {
            if (isupper(c)) capitals++;
        }
        return capitals == 0 || capitals == word.length() || (capitals == 1 && isupper(word[0]));
    }
};