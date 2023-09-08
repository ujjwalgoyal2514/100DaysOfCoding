class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #return sorted(s)==sorted(t)
        if len(t)>len(s):
            return False
        count={}
        for i in s:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        for j in  t:
            if j in count:
                count[j]-=1
            else:
                count[j]=1
        for k in count:
            if count[k]>0:
                return False
        return True