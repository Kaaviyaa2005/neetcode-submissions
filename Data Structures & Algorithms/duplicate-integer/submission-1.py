class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = set()
        isdup = False
        for i in nums:
            if i not in a:
                a.add(i)
            else:
                isdup = True
        return isdup
        