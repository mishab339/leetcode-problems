import heapq
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num,0) + 1
        
        pq = []

        for num, count in freq.items():
            if len(pq) < k:
                heapq.heappush(pq, (count, num))
            else:
                heapq.heappush(pq, (count, num))
                heapq.heappop(pq)
        
        res = []
        while pq:
            res.append(heapq.heappop(pq)[1])
        
        return res