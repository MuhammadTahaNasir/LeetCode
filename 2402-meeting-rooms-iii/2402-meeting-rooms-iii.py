import heapq

class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        # In-place sort
        meetings.sort()
        
        # Min-heaps
        avail = list(range(n))
        heapq.heapify(avail)
        busy = []  # (end, room)
        
        count = [0] * n
        
        for s, e in meetings:
            dur = e - s
            
            # Free rooms
            while busy and busy[0][0] <= s:
                heapq.heappush(avail, heapq.heappop(busy)[1])
            
            if avail:
                r = heapq.heappop(avail)
                heapq.heappush(busy, (e, r))
            else:
                end0, r = heapq.heappop(busy)
                heapq.heappush(busy, (end0 + dur, r))
            
            count[r] += 1
        
        # Find max index without builtin max+index duo
        best = 0
        mc = count[0]
        for i in range(1, n):
            if count[i] > mc:
                mc = count[i]
                best = i
        return best
