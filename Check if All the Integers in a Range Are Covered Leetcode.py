class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        l=[]
        for i in range(left,right+1):
            l.append(i)
        for j in ranges:
            for k in range(j[0],j[1]+1):
                if k in l:
                    l.remove(k)
        if len(l)==0:
            return True
        return False