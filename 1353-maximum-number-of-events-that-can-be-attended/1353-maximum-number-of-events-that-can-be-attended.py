class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        # 1.  Sort by start‑day.
        events.sort()                       # O(n log n)

        n, i = len(events), 0
        day = 0
        pq  : list[int] = []                # min‑heap of current end‑days
        attended = 0

        while i < n or pq:                  # keep going while events remain
            # If nothing is active, jump straight to next start day
            if not pq:
                day = events[i][0]

            # 2.  Add all events that have started by `day`
            while i < n and events[i][0] <= day:
                heapq.heappush(pq, events[i][1])
                i += 1

            # 3.  Remove anything already expired
            while pq and pq[0] < day:
                heapq.heappop(pq)

            # 4.  Attend the event that finishes earliest
            if pq:
                heapq.heappop(pq)
                attended += 1
                day += 1                    # move to the next day

        return attended