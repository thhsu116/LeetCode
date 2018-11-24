https://leetcode.com/problems/trapping-rain-water/

# Dynamic programming, time complexity O(n), iterrate 3 times, space complexity O(n)
# https://leetcode.com/problems/trapping-rain-water/solution/
class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans = 0
        mx = 0
        max_lr = [0]*len(height)
        for i in range(len(height)):
            if height[i] > mx:
                max_lr[i] = height[i]
                mx = height[i]
            else:
                max_lr[i] = mx
        #print(max_lr)
        
        mx = 0
        max_rl = [0]*len(height)
        for i in range(len(height)-1, -1, -1):
            if height[i] > mx:
                max_rl[i] = height[i]
                mx = height[i]
            else:
                max_rl[i] = mx
        #print(max_rl)
                
        for i in range(len(height)):
            ans += min(max_lr[i], max_rl[i]) - height[i]
            
        return ans
        
# two pointers, iterate toward center, time complexity O(n), space complexity O(1)
# approach 2: http://www.cnblogs.com/grandyang/p/4402392.html
class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans = 0
        l, r = 0, len(height)-1
        while l < r:
            mn = min(height[l], height[r])
            if mn == height[l]:
                l += 1
                while l < r and height[l] < mn:
                    ans += mn - height[l]
                    l += 1
            else:
                r -= 1
                while l < r and height[r] < mn:
                    ans += mn - height[r]
                    r -= 1
        return ans
        
# use stack, time complexity O(n), space complexity O(n)
class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        stack = []
        ans = 0
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                top = stack[-1]
                stack.pop()
                if not stack:
                    break
                dis = i - stack[-1] - 1
                bounded_height = min(height[i], height[stack[-1]]) - height[top]
                ans += dis * bounded_height
            stack.append(i)
            
        return ans
