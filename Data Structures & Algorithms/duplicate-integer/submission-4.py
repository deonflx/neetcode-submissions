class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        c=[]
        for i in nums:
            if i  in c:
                return True
            c.append(i)    
        return False        

           
        