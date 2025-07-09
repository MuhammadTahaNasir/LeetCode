class Solution {
public:
  int maxFreeTime(int eventTime, int k, const vector<int>& startTime, const vector<int>& endTime) {
    int n = startTime.size();
    vector<int> gaps;
    gaps.reserve(n + 1);

    // Compute all gaps in one pass (no branching in critical loop)
    gaps.push_back(startTime[0]);
    for (int i = 1; i < n; ++i)
      gaps.push_back(startTime[i] - endTime[i - 1]);
    gaps.push_back(eventTime - endTime[n - 1]);

    // Sliding window of size k + 1
    int maxFree = 0, windowSum = 0;
    int total = gaps.size();

    // Initial window
    for (int i = 0; i <= k && i < total; ++i)
      windowSum += gaps[i];
    maxFree = windowSum;

    // Slide the window
    for (int i = k + 1; i < total; ++i) {
      windowSum += gaps[i] - gaps[i - k - 1];
      if (windowSum > maxFree)
        maxFree = windowSum;
    }

    return maxFree;
  }
};
