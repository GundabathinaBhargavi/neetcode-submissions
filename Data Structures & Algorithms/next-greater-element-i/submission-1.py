class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n=len(nums2)
        res=[]
        for i in nums1:
            nextgre=-1
            for j in range(n-1,-1,-1):
                if nums2[j]>i:
                    nextgre=nums2[j]
                elif nums2[j]==i:
                    break
            res.append(nextgre)

                    
        return res