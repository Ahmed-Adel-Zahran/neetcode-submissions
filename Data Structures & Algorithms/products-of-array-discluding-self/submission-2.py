class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            print("res1:" ,res[i])
            prefix *= nums[i]

        
        suffix = 1
        for i in range(len(nums) -1 , -1 , -1):
            res[i] *= suffix
            print("res2:" ,res[i])
            suffix *= nums[i]
        return res