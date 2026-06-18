class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_count = {}
        for ch in s:
            if s not in s_count:
                s_count[ch] = s.count(ch)

        for key in s_count:
            if s_count[key] != t.count(key):
                return False       

        return True         