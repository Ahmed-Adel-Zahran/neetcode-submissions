class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1
        zero_count = nums.count(0)
         
        for num in nums:
            if(num != 0):
                total_product = total_product * num
            else:
                continue
              
        
        res = []
        for i in range (len(nums)):
            if nums[i] == 0:
                if zero_count > 1:
                    res.append(0)
                else:
                    res.append(int(total_product))
            elif 0 in nums:
                res.append(0)
            else:
                res.append(int(total_product / nums[i]))
        return res
