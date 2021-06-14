class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def pref(word):
            ans=[]
            for i in range(len(word)):
                if word[i:]==word[i:][::-1]:
                    ans.append(word[:i])
            return ans
        def suff(word):
            ans=[]
            for i in range(len(word)):
                if word[:i+1]==word[:i+1][::-1]:
                    ans.append(word[i+1:])
            return ans
        
        dic={word:i for i,word in enumerate(words)}
        ans=[]
        for i,word in enumerate(words):
            rev=word[::-1]
            if rev in dic:
                j=dic[rev]
                if i!=j:
                    ans.append((i,j))
            for pre in pref(word):
                rpre=pre[::-1]
                if rpre in dic:
                    ans.append((i,dic[rpre]))
            for suf in suff(word):
                rsuf=suf[::-1]
                if rsuf in dic:
                    ans.append((dic[rsuf],i))
        return ans
            
