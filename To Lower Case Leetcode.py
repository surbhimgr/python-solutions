class Solution:
    def toLowerCase(self, s: str) -> str:
        p=''
        for c in s:
            if ord(c)>=65 and ord(c)<91:
                k=ord(c)+32
                p+=chr(k)
            else:
                p+=c
        return p