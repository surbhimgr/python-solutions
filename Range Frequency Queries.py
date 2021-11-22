class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.arr=arr
        self.dic={}
        

    def query(self, left: int, right: int, value: int) -> int:
        string="".join(map(str,(left,right,value)))
        if string in self.dic.keys():
            return self.dic[string]
        else:
            ans=self.arr[left:right+1].count(value)
            self.dic[string]=ans
            return ans
        


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)
