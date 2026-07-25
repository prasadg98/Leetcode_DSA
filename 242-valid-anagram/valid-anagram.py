class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        Count_s = {}
        Count_t = {}

        for char in s:
            Count_s[char] = Count_s.get(char, 0) + 1

        for char in t:
            Count_t[char] = Count_t.get(char, 0) + 1

        return Count_s == Count_t 

        