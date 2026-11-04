class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for n in nums:
            if n not in hashmap:
                hashmap[n]=0
            hashmap[n]=hashmap[n]+1
        sorted_hashmap = sorted(hashmap,key=hashmap.get,reverse = True)
        return sorted_hashmap[:k]
        
        