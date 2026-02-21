from collections import Counter

class Solution:
    def relativeSortArray(self, arr1, arr2):
        count = Counter(arr1)
        result = []
        # return count
        for num in arr2:
            result += [num] * count[num]

        leftovers = []
        for num in arr1:
            if num not in arr2:
                leftovers.append(num)

        return result + sorted(leftovers)