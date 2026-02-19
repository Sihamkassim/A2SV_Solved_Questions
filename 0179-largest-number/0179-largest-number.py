class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        # print (nums)
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[j] + nums[i] > nums[i] + nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]

        result = ''.join(nums)
        return '0' if result[0] == '0' else result