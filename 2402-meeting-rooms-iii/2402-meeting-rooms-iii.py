import heapq

class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        meetings.sort()
        
        available = list(range(n))  # Free room IDs (min-heap)
        heapq.heapify(available)
        
        busy = []  # (end_time, room_id)
        count = [0] * n  # Meeting count per room

        for start, end in meetings:
            duration = end - start

            # Free up all rooms that are done before this meeting starts
            while busy and busy[0][0] <= start:
                heapq.heappush(available, heapq.heappop(busy)[1])

            if available:
                room = heapq.heappop(available)
                heapq.heappush(busy, (end, room))
            else:
                earliest_end, room = heapq.heappop(busy)
                heapq.heappush(busy, (earliest_end + duration, room))
            count[room] += 1

        # Return the room with the most meetings (break ties by smaller index)
        max_count = -1
        best_room = -1
        for i, c in enumerate(count):
            if c > max_count:
                max_count = c
                best_room = i
        return best_room
