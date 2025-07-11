class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        meetings.sort(key=lambda x: x[0])
        
        count = [0] * n
        available = list(range(n))
        heapq.heapify(available)
        
        # Encode occupied as integers
        # val = end_time * (n + 1) + room_id
        occupied = []
        base = n + 1
        
        for start, end in meetings:
            # Free rooms whose meetings ended by 'start'
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
        return count.index(max_count)
