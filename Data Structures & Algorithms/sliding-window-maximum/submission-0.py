from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        q = deque()  
        l = 0

        for r in range(len(nums)):

            # Remove smaller elements from the back
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            q.append(r)

            # Remove elements outside the window
            if q[0] < l:
                q.popleft()

            # Window has reached size k
            if r + 1 >= k:
                result.append(nums[q[0]])
                l += 1

        return result