class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max = 0
        current_max = 0
        for num in nums:
            if (num == 1):
                current_max +=1
                print(current_max)
                if(current_max > max):
                    max = current_max
            else:
                current_max = 0
            
        return max            

        