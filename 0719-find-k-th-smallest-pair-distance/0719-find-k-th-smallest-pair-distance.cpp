class Solution {
public:
    int smallestDistancePair(vector<int>& v, int k) {
        // Sort the input vector
        sort(v.begin(), v.end());
        
        // Binary search for the smallest possible distance
        int low = 0;
        int high = v.back() - v.front();
        
        while (low < high) {
            int mid = low + (high - low) / 2;
            if (countPairs(v, mid) < k) {
                low = mid + 1;
            } else {
                high = mid;
            }
        }
        
        return low;
    }
    
private:
    // Helper function to count the number of pairs with distance <= mid
    int countPairs(const vector<int>& v, int mid) {
        int count = 0;
        int n = v.size();
        int j = 0;
        
        for (int i = 0; i < n; ++i) {
            while (j < n && v[j] - v[i] <= mid) {
                ++j;
            }
            count += (j - i - 1);
        }
        
        return count;
    }
};
