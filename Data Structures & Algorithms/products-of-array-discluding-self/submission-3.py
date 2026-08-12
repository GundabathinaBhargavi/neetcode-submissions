class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res,zero=1,0
        for i in nums:
            if i:
                res*=i
            else:
                zero+=1
        if zero>1 :return [0]*len(nums)
        arr=[0]*len(nums)
        for i,j in enumerate(nums):
            if zero:arr[i]=0 if j else res
            else: arr[i]=res//j
        return arr
            

