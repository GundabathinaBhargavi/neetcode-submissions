class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        total_sum=nums[0]
        store=0
        j=0
        for i in range(1,len(nums)):
            if nums[i]>nums[j]:
                total_sum=total_sum+nums[i]
            else:
                store=max(total_sum,store)
                total_sum=nums[i]
            j+=1
        
        return max(store,total_sum)