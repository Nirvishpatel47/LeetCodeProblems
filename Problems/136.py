class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        di = {}
        for i in nums:
            di[i] = di.get(i, 0) + 1
        result = [k for k, v in di.items() if v == 1]
        return result[0]