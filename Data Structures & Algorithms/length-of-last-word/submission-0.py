class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.split()
        s.reverse()
        return len(s[0])
