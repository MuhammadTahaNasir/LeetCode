class Solution {
public:
    bool wordPattern(string pattern, string s) {
        vector<string> words;
        stringstream ss(s);
        string word;
        while (ss >> word) words.push_back(word);
        if (pattern.length() != words.size()) return false;
        unordered_map<char, string> char_map;
        unordered_map<string, char> word_map;
        for (int i = 0; i < pattern.length(); ++i) {
            char c = pattern[i];
            string w = words[i];
            if (char_map.count(c) && char_map[c] != w) return false;
            if (word_map.count(w) && word_map[w] != c) return false;
            char_map[c] = w;
            word_map[w] = c;
        }
        return true;
    }
};