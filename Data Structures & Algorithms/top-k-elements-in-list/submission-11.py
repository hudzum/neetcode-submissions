class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #hashmap
        #sort based on frequencies
        #pop k amount = onlogn for each element from sorting

        #min heap 
        #add to a hashmap
        # add to a minheap keep size to k
        # inseration cost log (size of element)
        # inseration would logk 
        # for each element O(nlogk)

        #Bucket Sort
        dic = defaultdict(int)
        for n in nums:
            dic[n] += 1

        #Put it into an array based on frequency
        #all of element with count = 2 are index = 2 
        #starting from 1 
        freq = [[] for i in range(len(nums)+1)]
        for number, frequency in dic.items():
            freq[frequency].append(number)
        results = []
        for li in reversed(freq):
            for ele in reversed(li):
                results.append(ele)
                if len(results) == k:
                    return results


