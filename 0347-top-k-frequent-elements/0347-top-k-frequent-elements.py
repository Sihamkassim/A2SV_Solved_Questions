class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        diff={}
        ans=[]
        for i in range(len(nums)):
            if nums[i] not in diff:
                diff[nums[i]]=1
            else:
                diff[nums[i]]+=1
        li1=list(diff.values())
        list1=sorted(li1 , reverse=True)
        for i in range(k):
            for key , value in diff.items():
                if value==list1[i]:
                    ans.append(key)
        return list(set(ans))


        