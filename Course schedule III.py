import collections
import heapq
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda k:k[1])
        mheap=[]
        cur=0
        for d,last in courses:
            if cur+d<=last:    
                heapq.heappush(mheap,-d)
                cur+=d
            elif mheap and -mheap[0]>d:
                cur+=d+heapq.heappop(mheap)
                heapq.heappush(mheap,-d)
        return len(mheap)