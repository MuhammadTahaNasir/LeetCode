import heapq

class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        meetings.sort()
        free = list(range(n))
        heapq.heapify(free)
        busy = []  # min‑heap of (end_time, room_id)
        count = [0] * n

        for s, e in meetings:
            dur = e - s
            # Reclaim rooms that have freed up
            while busy and busy[0][0] <= s:
                heapq.heappush(free, heapq.heappop(busy)[1])
            if free:
                r = heapq.heappop(free)
                heapq.heappush(busy, (e, r))
            else:
                end0, r = heapq.heappop(busy)
                heapq.heappush(busy, (end0 + dur, r))
            count[r] += 1

        # Choose the most-used room (ties broken by lowest index)
        best = 0
        for i in range(1, n):
            if count[i] > count[best]:
                best = i
        return best
