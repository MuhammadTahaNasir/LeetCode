class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        int counts[26] = { 0 };
        for (char c : magazine) counts[c - 'a']++;
        for (char c : ransomNote) {
            if (--counts[c - 'a'] < 0) return false;
        }
        return true;
    }
};