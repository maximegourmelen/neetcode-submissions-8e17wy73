class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss = sorted(list(s))
        st = sorted(list(t))
        return ss == st
     
        
        