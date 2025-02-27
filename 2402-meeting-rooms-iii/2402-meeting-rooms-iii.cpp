class Solution {
public:
    int mostBooked(int n, vector<vector<int>>& meetings) {
        sort(meetings.begin(), meetings.end());

        vector<int> count(n, 0); // Meeting count per room
        priority_queue<int, vector<int>, greater<>> available;
        for (int i = 0; i < n; ++i) available.push(i);

        // Min-heap: {endTime, roomId}
        priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<>> busy;

        for (auto& m : meetings) {
            long long start = m[0], end = m[1], duration = end - start;

            // Free up rooms that are done by current meeting's start
            while (!busy.empty() && busy.top().first <= start) {
                available.push(busy.top().second);
                busy.pop();
            }

            if (!available.empty()) {
                int room = available.top(); available.pop();
                busy.emplace(end, room);
                ++count[room];
            } else {
                auto [next_free_time, room] = busy.top(); busy.pop();
                busy.emplace(next_free_time + duration, room);
                ++count[room];
            }
        }

        int maxMeetings = 0, bestRoom = 0;
        for (int i = 0; i < n; ++i) {
            if (count[i] > maxMeetings) {
                maxMeetings = count[i];
                bestRoom = i;
            }
        }
        return bestRoom;
    }
};
