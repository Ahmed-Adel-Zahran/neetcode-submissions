class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if(len(nums) == 0):
            return False
        dic = Counter(nums)
        most_common = dic.most_common(1)
        return (most_common[-1][-1] > 1)

                    
         
        