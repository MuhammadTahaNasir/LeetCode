import heapq

class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        # Sort meetings by start time
        meetings.sort()
        
        # Heap of available room numbers (min-heap)
        available = list(range(n))
        heapq.heapify(available)
        
        # Heap of ongoing meetings as (end_time, room_id)
        busy = []
        
        # Count of meetings handled per room
        count = [0] * n

        for start, end in meetings:
            duration = end - start
            
            # Free up rooms that are done before the current meeting starts
            while busy and busy[0][0] <= start:
                end_time, room = heapq.heappop(busy)
                heapq.heappush(available, room)

            if available:
                # Assign to the available room with the smallest ID
                room = heapq.heappop(available)
                heapq.heappush(busy, (end, room))
                count[room] += 1
            else:
                # No rooms available: delay meeting to the earliest possible time
                end_time, room = heapq.heappop(busy)
                new_end = end_time + duration
                heapq.heappush(busy, (new_end, room))
                count[room] += 1

        # Return the room with max count, preferring the smallest index
        max_meetings = max(count)
        return count.index(max_meetings)
