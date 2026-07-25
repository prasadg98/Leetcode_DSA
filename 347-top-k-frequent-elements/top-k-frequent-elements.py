class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}
        for num in nums:
            freq_dict[num] = freq_dict.get(num, 0) + 1
        
        # index = frequency, value = list of numbers with that frequency
        new_arr = [[] for _ in range(len(nums) + 1)]
        
        for num, freq in freq_dict.items():
            new_arr[freq].append(num)
        
        # traverse from highest frequency to lowest, collecting k numbers
        result = []
        for freq in range(len(new_arr) - 1, 0, -1):
            for num in new_arr[freq]:
                result.append(num)
                if len(result) == k:
                    return result
        
        return result


            


