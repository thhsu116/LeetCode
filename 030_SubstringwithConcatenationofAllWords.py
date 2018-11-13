# https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/

# 29% 892ms, O(m*n), m = len(s), n=len(words)
class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        from collections import Counter
    
        def startsWithwords(string, _words):
            cnt = Counter(_words)
            i = 0
            word_length = len(_words[0])
            word_num = len(_words)
            while i < word_length*word_num:
                w = string[i: i+word_length]
                if cnt[w]:
                    cnt[w] -= 1
                    if cnt[w] == 0:
                        del cnt[w]
                    i += word_length
                else:
                    return False
            return True
            
        
        ans = []
        if not words:
            return ans
        word_length = len(words[0])
        if not all(len(word) == word_length for word in words) or len(s) < word_length*len(words):
            return ans
        
        counter = Counter(words)
        for i in range(len(s) - word_length*len(words)+1):
            if s[i:i+word_length] in counter:
                if startsWithwords(s[i:], words):
                    ans.append(i)
        return ans
        
# 76% 116ms, time complexity: O(n)
# https://leetcode.com/problems/substring-with-concatenation-of-all-words/discuss/191809/Detailed-explanation-and-Done-in-Python.
class Solution:
    def __init__(self):
        self.ans = []
        
    def findstring(self, start, end, ls, lw, lt, s, hashmap):
        # We will call the sliding window algorithm here.
        # Please make yourself aware of all the variables
        
        tmpmap = {}
        while end+lw <= ls:
            # Take each word and increment end
            word = s[end: end+lw]
            end = end + lw
            # If this word is not in the hashmap then this 
            # then we discard everything till now and move 
            # start to end position. I used continue for better 
            # readablility but we should use else
            if word not in hashmap:
                tmpmap.clear()
                start = end
            else:
                # If we come here it means we found "word" in the hashmap
                tmpmap[word] = tmpmap[word] + 1 if word in tmpmap else 1
            
                # This is the most crucial part of the algorithm.  Please
                # understand this part very carefully
                # let's understand by an example. If we find a word in our 
                # string more than it's occurence in list of words provided
                # it means that we need to discard all the words in the substring
                # till it becomes equal to hashmap
                # Example:
                # "wordgoodgoodgoodbestword"
                # ["word","good","best","word"]
                # Work through this example and this 
                # Example:
                # "wordgoodgoodgoodbestwordword"
                # ["word","good","best","word"]
                while tmpmap[word] > hashmap[word]:
                    tmpmap[s[start:start+lw]] -= 1
                    start = start + lw
            
                # Now check if we find an answer
                if end - start == lt:
                    self.ans.append(start)
                
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        # We will be using a sliding window logic here.
        
        #1. let's first check the basic validation.
        #This is self explanatory
        
        if len(s) == 0 or len(words) == 0 or len(words[0]) == 0:
            return []
        
        print ("are we coming here ")
        ls = len(s)             # Length of the full string
        lw = len(words[0])      # Length of each words in the string
        lt = len(words)* lw     # Lenght of all the words will be
        
        # Store all the word from the list to hash
        hashmap = collections.defaultdict(int) 
        for word in words:
            hashmap[word] += 1     
        
        # We only need to go minimum of the word lenght or total string  length - length of total words
        for i in range(0, min(lw, ls - lt + 1)):
            self.findstring(i, i, ls, lw, lt, s, hashmap)
        return self.ans
