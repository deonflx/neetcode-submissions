class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        cs,ct={},{}
        for i in range(len(s)):
            cs[s[i]]=s.count(s[i])
            ct[t[i]]=t.count(t[i])
        for c in cs:
            if cs[c]!=ct.get(c,0):
                return False    
        return True            
        