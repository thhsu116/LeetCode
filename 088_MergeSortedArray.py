# https://leetcode.com/problems/merge-sorted-array/

# 56ms 99%, use extra space to save nums1, time O(m+n) space O(m)
class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        tmp1 = nums1[:m]
        i, j, cnt = 0, 0, 0
        while i < m and j < n:
            #print(f'{i}, {j}')
            if tmp1[i] <= nums2[j]:
                nums1[cnt] = tmp1[i]
                i += 1
            else:
                nums1[cnt] = nums2[j]
                j += 1
            cnt += 1
        if i == m:
            nums1[cnt: m+n] = nums2[j:]
        if j == n:
            nums1[cnt: m+n] = tmp1[i:]
            
# 60ms 74%, merge inplace, time O(m+n), space O(1)
class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:m+n] = nums2
        if len(nums1) <= 1:
            return
        l = 0
        r = m
        while l < r and l < m+n and r < m+n:
            if nums1[l] < nums1[r]:
                l += 1
            else:
                r_num = nums1[r]
                nums1[l+1: r+1] = nums1[l: r]
                nums1[l] = r_num
                l += 1
                r += 1
