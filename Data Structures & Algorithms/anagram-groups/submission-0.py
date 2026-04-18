class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_l = []
        d = {}
        final_l = []
        for i in range(len(strs)):
            sorted_l.append(''.join(sorted(strs[i])))
        for i in range(len(strs)):
            if (sorted_l[i] in d.keys()) == True:
                d[sorted_l[i]].append(i)
            else:
                d[sorted_l[i]] = [i]
        for key, value in zip(d.keys(), d.values()):
            temp_l = []
            for element in value:
                temp_l.append(strs[element])
            final_l.append(temp_l)

        return final_l