# https://leetcode.com/problems/count-and-say/discuss/15999/4-5-lines-Python-solutions

# 17% 60ms, straight forward with recursive
class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        def cas(string):
            ret = ''
            prev = string[0]
            cnt = 0
            for s in string:
                if s == prev:
                    cnt += 1
                else:
                    ret += str(cnt)+prev
                    cnt = 1
                prev = s
            ret += str(cnt)+prev
                
            return ret
        
        string = '1'
        for _ in range(n-1):
            string = cas(string)
        
        return string
                
# pyhtonic solutions
# https://leetcode.com/problems/count-and-say/discuss/15999/4-5-lines-Python-solutions
def countAndSay(self, n):
    s = '1'
    for _ in range(n - 1):
        s = re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), s)
    return s
    
def countAndSay(self, n):
    s = '1'
    for _ in range(n - 1):
        s = ''.join(str(len(group)) + digit
                    for group, digit in re.findall(r'((.)\2*)', s))
    return s
    
def countAndSay(self, n):
    s = '1'
    for _ in range(n - 1):
        s = ''.join(str(len(list(group))) + digit
                    for digit, group in itertools.groupby(s))
    return s
