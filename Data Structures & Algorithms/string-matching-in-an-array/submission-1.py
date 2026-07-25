class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        sol=[]
        for i in words:
            for j in words:
                if i!=j and i in j :
                    sol.append(i)
                    break

        s=set(sol)
        return list(s)  