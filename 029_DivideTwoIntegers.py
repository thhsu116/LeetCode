# https://leetcode.com/problems/divide-two-integers/description/

# 98% 52ms, 
# 1. ans=0, shift divisor left one bit at a time, until divisor >= dividend
# 2. divisor shift right by 1, shift number -=1, if devidend > divisor ans += 1 << shift number
class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        def checkOverflow(ans):
            if ans < -2**31 or ans > 2**31-1:
                return 2**31-1
            else:
                return ans
        
        if dividend > 0 and divisor > 0 or dividend < 0 and divisor < 0:
            positive = True
        else:
            positive = False


        if abs(dividend) < abs(divisor):
            return 0
        elif dividend == divisor:
            return 1
        elif dividend + divisor == 0:
            return -1
        elif abs(divisor) == 1:
            if positive:
                return checkOverflow(abs(dividend))
            else:
                return checkOverflow(0-abs(dividend))

        shift_cnt = 0
        while abs(dividend) >= abs(divisor):
            divisor <<= 1
            shift_cnt += 1
        ans = 1 << (shift_cnt-1)

        if abs(dividend) == abs(divisor):
            if positive:
                return checkOverflow(ans)
            else:
                return checkOverflow(0-ans)

        divisor >>= 1
        shift_cnt -= 1
        dividend = abs(dividend) - abs(divisor)
        while shift_cnt >= 0:
            if abs(dividend) >= abs(divisor):
                dividend = abs(dividend) - abs(divisor)
                ans += 1 << shift_cnt
            divisor >>= 1
            shift_cnt -= 1


        if positive:
            return checkOverflow(ans)
        else:
            return checkOverflow(0-ans)

# no abs, no overflow

Created at: November 3, 2018 1:39 AM

cntcntcnt
cntcntcnt
 4
class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        pmax = 0x7fffffff
        nmax = -pmax - 1
        # This eliminates the handling of the overflow
        # of the quotient
        if dividend == nmax and divisor == -1:
            return pmax
        s_dividend = dividend
        s_divisor = divisor
        # instead of using abs(), we use negative number
        # to do division so that overflow will never occur
        # when the dividend is 0x80000000
        dividend = dividend if dividend < 0 else -dividend
        divisor = divisor if divisor < 0 else -divisor
        q = 0
        while dividend <= divisor:
            i = 0
            while (divisor << i) >= dividend:
                i += 1
            i -= 1    
            dividend -= divisor << i
            q += (1 << i)
        return q if (s_dividend>0) == (s_divisor>0) else -q
