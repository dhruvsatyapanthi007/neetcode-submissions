class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freqDict = collections.defaultdict(int)
        
        for n in nums:
            freqDict[n] += 1
        
        freqList = [(-value, key) for key, value in freqDict.items()]
        heapq.heapify(freqList)

        for i in range(0, k):
            res.append(heapq.heappop(freqList)[1])

        return res
