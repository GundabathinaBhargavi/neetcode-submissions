class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        h1,h2={},{}
        for i in range(len(s)):
            c,d = s[i],t[i]
            if (c in h1 and h1[c]!=d) or (d in h2 and h2[d]!=c):
                return False
            h1[c]=d
            h2[d]=c
        return True
        