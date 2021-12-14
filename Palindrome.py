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



#Manacher's Algorithm
class Solution2:
    bogus='|'

    def __init__(self):
        self.data = [self.bogus]
        self.radii = []
        self.center=0
        self.radius=0
        self.maxCenter=-1
        self.maxRadius=-1
    
    def longestPalindrome(self,string=""):
        for i in range(len(string)):
            self.data.extend([string[i],self.bogus])
        #initializing first element of radii for mirrored collection at element 0
        self.radii.append(0)
        for i in range(1,len(self.data)):
            self.compareCenter(i)
        left = (self.maxCenter-self.maxRadius)//2
        right = (self.maxCenter+self.maxRadius+1)//2
        s = string[left:right]
        return self.radii
    
    #Manacher's algorithm shortcut so you don't need to calculate mirrored non-edge cases
    def compareCenter(self,index):
        if index == 8:
            print(self.data[8])
        mirror = 2 * self.center - index
        if index + self.radii[mirror] < self.center + self.radius:
            self.radii.append(self.radii[mirror])
        else:
            if index < self.center + self.radius:
                currentRadius = self.radii[self.center]//2
            else:
                currentRadius = 0
            while (
                index - currentRadius > -1 and index + currentRadius < len(self.data) and 
                self.data[index-currentRadius] == self.data[index+currentRadius]
            ):
                currentRadius += 1
            currentRadius -=1 
            if index + currentRadius > self.center + self.radius:
                self.center = index
                self.radius = currentRadius
                if self.radius > self.maxRadius:
                    self.maxCenter = self.center
                    self.maxRadius = self.radius
            self.radii.append(currentRadius)
