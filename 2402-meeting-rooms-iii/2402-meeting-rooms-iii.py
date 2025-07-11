import heapq

class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        count = [0] * n
        
        # Sort meetings by start time
        meetings.sort(key=lambda x: x[0])
        
        # Min-heap for rooms currently occupied: (end_time, room_id)
        occupied = []
        
        # Min-heap for available room ids
        available = list(range(n))
        heapq.heapify(available)
        
        for start, end in meetings:
            # Release all rooms that have become free by 'start' time
            while occupied and occupied[0][0] <= start:
                freed_end, freed_room = heapq.heappop(occupied)
                heapq.heappush(available, freed_room)
            
            duration = end - start
            
            if available:
                # Assign meeting to the smallest available room
                room = heapq.heappop(available)
                count[room] += 1
                heapq.heappush(occupied, (end, room))
            else:
                # No room free at start time, delay meeting until earliest room frees up
                earliest_end, room = heapq.heappop(occupied)
                count[room] += 1
                new_end = earliest_end + duration
                heapq.heappush(occupied, (new_end, room))
        
        # Return room with the maximum meetings booked (lowest room id if tie)
        max_count = max(count)
        return count.index(max_count)
