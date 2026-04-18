class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        l = sorted(list(zip(d.values(), d.keys())))
        final_l = []
        for i in range(len(l)-1, len(l)-1-k, -1):
            final_l.append(l[i][1])

        return final_l