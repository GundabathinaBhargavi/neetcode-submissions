class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l = Counter(nums)
        return [i for i,j in l.most_common(k)]