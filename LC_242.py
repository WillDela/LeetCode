class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        countS, countT = {}, {}

        for char in s:
            if char in countS:
                countS[char]+=1
            else:
                countS[char]=1

        for char in t:
            if char in countT:
                countT[char]+=1
            else:
                countT[char]=1

        return countT == countS

# O(n) solution!

        """  
    this is the same as return countT == countS
        
        if countT == countS:
            return True
        else:
             return False


    different solution:

        if len(s) != len(t):
            return False
            
        count = {}

        for char in s:
            count[char] = count.get(char,0) + 1
        
        for char in t:
            count[char] = count.get(char,0) - 1

        for val in count.values():
            if val != 0:
                return False
                
        return True
        """