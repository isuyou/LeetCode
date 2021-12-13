from typing import Optional

class Solution:
    data = ""

    def __init__(self):
        self.data = ""

    def longestPalindrome(self,string=""):
        self.leftBound = 0
        self.rightBound = 0
        for i in range(len(string)):
            self.expandFromCenter(string,i,i)
            self.expandFromCenter(string,i,i+1)
        return string[self.leftBound:self.rightBound]

    def expandFromCenter(self, string, left, right):
        while (-1 < left) and (right < len(string)):
            if string[left] == string[right]:
                left -= 1
                right += 1
            else:
                break
        if right - left - 1 > self.rightBound - self.leftBound:
            self.leftBound = left + 1
            self.rightBound = right



class Solution2:
    bogus='|'

    def __init__(self):
        self.data = [bogus]
        self.center=0
        self.radius=0
    
    def longestPalindrome(self,string=""):
        for i in range(len(string)):
            self.data.extend([string[i],bogus])
        for i in range(len(bogus))
            compareCenter(string,i)
    
    def compareCenter(self,string,index):
