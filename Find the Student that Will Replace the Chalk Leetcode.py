class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        l=len(chalk)
        s=sum(chalk)
        rc=k%s
        for i in range(l):
            rc=rc-chalk[i]
            if rc<0:
                return i