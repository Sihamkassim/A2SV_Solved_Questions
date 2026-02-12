class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        even_sum = sum(x for x in nums if x % 2 == 0)

        for val, idx in queries:
            old = nums[idx]

            if old % 2 == 0:
                even_sum -= old

            nums[idx] = old + val

            if nums[idx] % 2 == 0:
                even_sum += nums[idx]

            res.append(even_sum)

        return res
