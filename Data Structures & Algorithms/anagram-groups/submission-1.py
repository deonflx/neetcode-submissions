class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        op=[]
        r=[]
        for i in range(len(strs)):
            s=strs[i]
            if i in r :
                continue
            temp=[s]
            for j in range(i+1,len(strs)):
                t=strs[j]
                if len(s)!=len(t):
                    continue
                cs,ct={},{}
                for i in range(len(s)):
                    cs[s[i]]=1+cs.get(s[i],0)
                    ct[t[i]]=1+ct.get(t[i],0)
                w=0
                for c in cs:
                    if cs[c]!=ct.get(c,0):
                        w=1
                        break
                if w==1:
                    continue
                if j not in r:
                    temp.append(t)
                    r.append(j)
            op.append(temp)             
        return op