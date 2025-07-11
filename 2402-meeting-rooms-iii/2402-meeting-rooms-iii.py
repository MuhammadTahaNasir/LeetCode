import heapq

class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        meetings.sort(key=lambda x: x[0])
        
        count = [0] * n
        available = list(range(n))
        heapq.heapify(available)
        
        base = n + 1  # base for encoding
        occupied = []  # store as single int: end_time * base + room_id
        
        for start, end in meetings:
            # Release rooms that got free before current meeting starts
            while occupied and (occupied[0] // base) <= start:
                val = heapq.heappop(occupied)
                room = val % base
                heapq.heappush(available, room)
            
            duration = end - start
            
            if available:
                room = heapq.heappop(available)
                count[room] += 1
                heapq.heappush(occupied, end * base + room)
            else:
                val = heapq.heappop(occupied)
                earliest_end = val // base
                room = val % base
                count[room] += 1
                heapq.heappush(occupied, (earliest_end + duration) * base + room)
        
        max_count = max(count)
        # Return smallest room ID if tie (count.index does this naturally)
        return count.index(max_count)
