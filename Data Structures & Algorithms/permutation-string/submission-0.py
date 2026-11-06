class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        c1={}
        c2={}
        l=0
        for ch in s1:
            c1[ch]=c1.get(ch,0)+1
        for r in range(len(s2)):
            c2[s2[r]]=c2.get(s2[r],0)+1
            if r-l+1>len(s1):
                c2[s2[l]]-=1
                if c2[s2[l]]==0:
                    del c2[s2[l]]
                l+=1
            if c1==c2:
                return True
        return False