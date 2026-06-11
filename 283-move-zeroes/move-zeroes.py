class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:          # found a non-zero
                nums[left], nums[right] = nums[right], nums[left]  # swap it forward
                left += 1                 # left only moves here


        


                



        


                

                


       

            

        