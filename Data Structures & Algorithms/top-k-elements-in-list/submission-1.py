class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freqDict = collections.defaultdict(int)
        
        for n in nums:
            freqDict[n] += 1
        
        heap = []
        for key, value in freqDict.items():
            heapq.heappush(heap, (freqDict[key], key))
            if len(heap) > k:
                heapq.heappop(heap)

        for i in range(0, k):
            res.append(heapq.heappop(heap)[1])

        return res
