class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count={}
        for i in nums:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        for k in count:
            if count[k]>1:
                return True
        return False   