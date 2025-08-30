class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        int m = s1.size();
        int n = s2.size();

        if (m > n) return false;

        vector<int> s1map(26, 0);
        vector<int> s2map(26, 0);

        // Initialize the frequency maps for s1 and the first window of s2
        for (int i = 0; i < m; ++i) {
            ++s1map[s1[i] - 'a'];
            ++s2map[s2[i] - 'a'];
        }

        // Sliding window over s2
        for (int i = m; i < n; ++i) {
            if (s1map == s2map) return true;
            
            // Slide the window by removing the leftmost element and adding the new element
            ++s2map[s2[i] - 'a'];
            --s2map[s2[i - m] - 'a'];
        }

        // Check the last window
        return s1map == s2map;
    }
};
