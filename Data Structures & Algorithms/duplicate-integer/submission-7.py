class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if(len(nums) == 0):
            return False
        dic = Counter(nums)
        return max(dic.values()) > 1

                    
         
        