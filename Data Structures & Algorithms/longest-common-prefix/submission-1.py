class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = strs[0]
        for word in strs[1:]:
            i=0
            while i<len(longest) and i<len(word):
                if longest[i]!=word[i]:
                    break
                i+=1
            longest = longest[:i]
        return longest