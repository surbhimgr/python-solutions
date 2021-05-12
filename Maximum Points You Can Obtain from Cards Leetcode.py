class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l=len(cardPoints)
        s=0
        i=0
        j=0
        ans=sys.maxsize
        for j,n in enumerate(cardPoints):
            s+=n
            if j-i>l-k-1:
                s-=cardPoints[i]
                i+=1
            if j-i==l-k-1:
                ans=min(ans,s)

        return sum(cardPoints)-ans