class Solution:
    def maxDifference(self, s: str) -> int:
        from collections import Counter
        odd = float('-inf')
        even= float('inf')
        cnt = Counter(s)
        for i in cnt.values():
            if i%2 :
                odd= max(odd,i)
            else:
                even=min(even,i)
        return odd-even
