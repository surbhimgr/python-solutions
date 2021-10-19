from collections import defaultdict
currtime=5
class Dic():
    def __init__(self):
        self.d=defaultdict(list)
    def actualinsert(self,key,value,time):
        self.d[key].append(value)
        self.d[key].append(time)
    def update(self,key,value,time):
        self.d[key][0]=value
        self.d[key][1]=time
    def insert(self,key,value,time):
        if key in self.d.keys():
            self.update(key,value,time)
        else:
            self.actualinsert(key,value,time)
    def checkdeadline(self,key):
        if self.d[key][1]>currtime:
            return False
        return True
    
d1=Dic()
d1.insert(1,2,3)
d1.insert(1,2,7)
print(d1.checkdeadline(1))
