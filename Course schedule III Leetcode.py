import collections
import heapq   #for making a max heap
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda k:k[1])    #sorts the courses list according to the last day 
        mheap=[]
        curtime=0
        for duration,lastday in courses:
            if curtime+duration<=lastday:    #fitting in schedule, no conflicts
                heapq.heappush(mheap,-duration)     #add the negation of duration to the heap as it by default works as minheap so we have to put an additional '-' sign to make it work as maxheap
                curtime+=duration              #add the total time
            elif mheap and -mheap[0]>duration:      #maximum of the previously added durations are greater than the current duration
                #we will swap the current duration and the maximum duration
                curtime+=duration+heapq.heappop(mheap)  #total time equals to current schedule duration - maximum from the previously added durations (we use plus here because the negation of duration was added to the heap so basiclly they are substracted)
                heapq.heappush(mheap,-duration)
        return len(mheap) #return length of the heap as it has all the durations scheduled
