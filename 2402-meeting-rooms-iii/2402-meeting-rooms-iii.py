import heapq

class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        count = [0] * n
        meetings.sort(key=lambda x: x[0])
        
        occupied = []  # (end_time, room_id)
        available = list(range(n))
        heapq.heapify(available)
        
        for start, end in meetings:
            while occupied and occupied[0][0] <= start:
                _, room = heapq.heappop(occupied)
                heapq.heappush(available, room)
            
            duration = end - start
            
            if available:
                room = heapq.heappop(available)
                count[room] += 1
                heapq.heappush(occupied, (end, room))
            else:
                earliest_end, room = heapq.heappop(occupied)
                count[room] += 1
                heapq.heappush(occupied, (earliest_end + duration, room))
        
        max_count = max(count)
        return count.index(max_count)
