class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c={}
        for i in  nums:
            c[i]=1+c.get(i,0)
        r=[]
        for i in range(k):
            g=0
            p=0
            for j in c:
               if c[j] >g:
                g=c[j]
                p=j
            
            r.append(p)
            del c[p]
        return r         
        