class Solution {
public:
  int maxFreeTime(int eventTime, int k, const vector<int>& startTime, const vector<int>& endTime) {
    int n = startTime.size();
    int windowSum = 0, maxFree = 0;

    // Helper lambda to compute the gap at position i
    auto getGap = [&](int i) -> int {
      if (i == 0) return startTime[0];  // Before first event
      if (i == n) return eventTime - endTime.back();  // After last event
      return startTime[i] - endTime[i - 1];  // Between events
    };

    // Step 1: Initial window sum of size k+1
    for (int i = 0; i <= k && i <= n; ++i)
      windowSum += getGap(i);
    maxFree = windowSum;

    // Step 2: Slide the window
    for (int i = k + 1; i <= n; ++i) {
      windowSum += getGap(i) - getGap(i - k - 1);
      maxFree = max(maxFree, windowSum);
    }

    return maxFree;
  }
};
