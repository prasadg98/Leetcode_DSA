class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen ={}
        for num in nums:
            seen[num] = seen.get(num, 0) + 1
        
        sorted_keys = sorted(seen, key=lambda num: seen[num], reverse=True)
        return sorted_keys[:k]
            

        