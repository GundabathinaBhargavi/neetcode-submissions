class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = strs[0]
        for i in range(1,len(strs)):
            j,k=0,0
            word=strs[i]
            while j<len(longest) and k<len(word):
                if word[k] == longest[j]:
                    k+=1
                    j+=1
                else :
                    break
            if j==0 and k==0:
                longest=""
            else:
                longest=word[:k]
        return longest