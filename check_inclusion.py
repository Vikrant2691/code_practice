
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False

        hm_s1 = [0]*26
        hm_s2 = [0]*26
        matches = 26
        for i in range(len(s1)):
            hm_s1[ord(s1[i])-ord('a')]+=1
            hm_s2[ord(s2[i])-ord('a')]+=1
        
        for i in range(len(hm_s1)):
            if hm_s1[i]!=hm_s2[i]:
                matches-=1
        
        l,r=0,len(s1)-1
        
        for r in range(len(s1),len(s2)):
            
            if matches==26:
                return True
            
            hm_s2[ord(s2[r])-ord('a')] +=1
            
            if hm_s1[ord(s2[r])-ord('a')]==hm_s2[ord(s2[r])-ord('a')]:
                matches+=1
            else:
                matches-=1
            
            
            hm_s2[ord(s2[l])-ord('a')] -= 1
            
            if hm_s1[ord(s2[l])-ord('a')]==hm_s2[ord(s2[l])-ord('a')]:
                matches+=1
            else:
                matches-=1
            l+=1
            
        
        return matches==26


print(Solution().checkInclusion("abc","bbbca"))
# print(Solution().checkInclusion("abc","lecaabee"))
# print(Solution().checkIn`clusion("adc","dcda"))