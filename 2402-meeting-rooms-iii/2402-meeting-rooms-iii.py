import heapq

class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        meetings.sort()

        count = [0] * n  # Meeting counts
        free = list(range(n))  # Available room numbers (heap)
        heapq.heapify(free)

        busy = []  # (end_time, room_id)

        for start, end in meetings:
            duration = end - start

            # Free up rooms
            while busy and busy[0][0] <= start:
                heapq.heappush(free, heapq.heappop(busy)[1])

            if free:
                room = heapq.heappop(free)
                heapq.heappush(busy, (end, room))
            else:
                end_time, room = heapq.heappop(busy)
                heapq.heappush(busy, (end_time + duration, room))
            count[room] += 1

        # Find the room with max meetings (lowest index if tie)
        max_meetings = max(count)
        for i in range(n):
            if count[i] == max_meetings:
                return i
