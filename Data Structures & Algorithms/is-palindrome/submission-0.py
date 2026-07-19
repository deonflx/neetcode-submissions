class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        a=[]
        for i in s:
            if i.isalnum():
                a.append(i)
        if a[::-1] == a:
            return True
        return False    
