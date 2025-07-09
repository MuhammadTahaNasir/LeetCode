class Solution {
 public:
  int maxFreeTime(int eventTime, int k, vector<int>& startTime,
                  vector<int>& endTime) {
    int n = startTime.size();
    vector<int> gaps;
    gaps.reserve(n + 1);  // Reserve to avoid reallocations

    // First gap (before the first event)
    gaps.push_back(startTime[0]);

    // Gaps between events
    for (int i = 1; i < n; ++i) {
      gaps.push_back(startTime[i] - endTime[i - 1]);
    }

    // Last gap (after the last event)
    gaps.push_back(eventTime - endTime.back());

    // Sliding window of size (k + 1)
    int windowSum = 0;
    for (int i = 0; i <= k && i < gaps.size(); ++i)
      windowSum += gaps[i];

    int maxFree = windowSum;

    for (int i = k + 1; i < gaps.size(); ++i) {
      windowSum += gaps[i] - gaps[i - k - 1];
      maxFree = max(maxFree, windowSum);
    }

    return maxFree;
  }
};
