# https://leetcode.com/problems/multiply-strings/

# 18%, 272ms, time complexity O(mn), space complexity O(mn)
class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'
        
        products = [[] for _ in range(len(num2))]
        
        for i in range(len(num2)-1, -1, -1):
            
            for _ in range(len(num2) - 1 - i):
                products[i].append(0)
            
            carry = 0
            for j in range(len(num1)-1, -1, -1):
                p = (ord(num1[j]) - ord('0'))* (ord(num2[i]) - ord('0')) + carry
                carry = p // 10
                products[i].append(p % 10)
            
            if carry > 0:
                products[i].append(carry)
        #print(products)        
        ret = []
        carry = 0
        for i in range(len(products[0])):
            _sum = 0 + carry
            for p in products:
                try:
                    _sum += p[i]
                except:
                    pass
            ret.append(chr((_sum % 10) + ord('0')))
            carry = _sum // 10
        
        if carry > 0:
            ret.append(chr(carry + ord('0')))
        ret.reverse()
        
        return ''.join(ret)
     
# time complexity: O(mn), space complexity O(m+n)
def multiply(self, num1, num2):
        res = [0]* (len(num1) + len(num2))
        for i, e1 in enumerate(reversed(num1)):
            for j, e2 in enumerate(reversed(num2)):
                res[i+j] += int(e1) * int(e2)
                res[i+j+1] += res[i+j]/10
                res[i+j] %= 10
    
        while len(res) > 1 and res[-1] == 0: res.pop()
        return ''.join( map(str,res[::-1]) )
