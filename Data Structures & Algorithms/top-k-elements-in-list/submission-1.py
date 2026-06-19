class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        for n in nums:
            dic[n] += 1

        minheap =[]
        for key in dic.keys():
            heapq.heappush(minheap, ( dic[key],key))
            if len(minheap)>k:
                heapq.heappop(minheap)
        result = []
        for i in range(k):
            result.append(heapq.heappop(minheap)[1])

        return result