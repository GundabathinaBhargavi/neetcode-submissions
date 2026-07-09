class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        right=-1
        for i in range(len(arr)-1,-1,-1):
            temp=arr[i]
            arr[i]=right
            right=max(temp,right)
        return arr
        


