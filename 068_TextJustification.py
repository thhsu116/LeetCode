# https://leetcode.com/problems/text-justification/

# 32ms 100%, 
class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        # grouping words
        start = 0
        l = 0
        just = []
        for i in range(len(words)):
            l += len(words[i])
            if l + i - start > maxWidth:
                just.append(words[start: i])
                start = i
                l = len(words[i])
        just.append(words[start:])

        # inserting spaces between words in each group
        res = []
        while just:
            j = just.pop(0)
            if len(just) == 0:
                fj = ' '.join(j)
                res.append(fj + ' '*(maxWidth - len(fj)))
                return res
            
            for i in range(maxWidth - len(''.join(j))):
                j[i % (len(j)-1 or 1)] += ' '  # insert one space, except after the last word, at a time in round robin fashion
            res.append(''.join(j))
