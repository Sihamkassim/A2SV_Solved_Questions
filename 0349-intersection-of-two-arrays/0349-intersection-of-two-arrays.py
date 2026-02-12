class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # intersection_list=list(set(nums1).intersection(nums1))
        # return (intersection_list)

        intersection_set=set(nums1)&set(nums2)
        intersection_list=list(intersection_set)
        return (intersection_list)



        