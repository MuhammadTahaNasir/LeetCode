class Solution {
public:
    string removeOccurrences(string s, string part) {
        int partLen = part.size();
        size_t pos;
        
        // Continuously search for the `part` and remove it from `s`
        while ((pos = s.find(part)) != string::npos) {
            s.erase(pos, partLen);
        }
        
        return s;
    }
};
