class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums)+1)]
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
    
        results = []
        for key, item in count.items():
            freq[item].append(key)

        print(freq)
        for num in reversed(freq):
            for n in reversed(num):
                results.append(n)
                if len(results) == k:
                    return results

            

