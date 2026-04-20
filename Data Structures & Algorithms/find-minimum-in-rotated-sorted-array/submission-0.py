class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0 , len(nums)-1
        res = nums[0]

        while l <= r:
            if(nums[l] < nums[r]):
                res = min(res, nums[l])
                break
            
            
            midIdx = (l + r) // 2
            mid = nums[midIdx]
            if mid >= nums[l]:
                l = midIdx + 1
            else :
                r = midIdx - 1 
            
            res = min(res, nums[midIdx])  
        return res
