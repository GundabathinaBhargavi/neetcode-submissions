class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt,maxi=0,0
        for i in nums:
            if i==1:
                cnt+=1
            if i==0:
                maxi=max(cnt,maxi)
                cnt=0
        maxi=max(cnt,maxi)
        return maxi
            