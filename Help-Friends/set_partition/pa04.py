class Set:
    def __init__(self,V):
        self._elements = V

    def Elements(self):
        v = []
        for i in self._elements:
            v.append(i)
            v.sort()
        return v

class Partition:
    def __init__(self,V):
        self.Sets=[]
        for i in V:
            if V.count(i) > 1:
                raise Exception('invalid operation')
            else:
                self.Sets.append([i])
        self.l=[]
    def __str__(self):
        return str(self.Sets)
    def MakeSet(self,a):
        for i in self.Sets:
            for j in i:
                if a == j:
                  raise Exception('invalid operation')  
        else:
            self.Sets.append([a])
    def FindSet(self,a):
        for i in self.Sets:
            for j in i:
                if a == j:
                    return i[0]
        else:
            raise Exception('invalid operation')
    def Union(self,a,b):
        l = []
        for m in self.Sets:
            for n in m:
                l.append(n)
        if a not in l:
            raise Exception('invalid operation')
        if b not in l:
            raise Exception('invalid operation') 
        for i in self.Sets:
            for j in self.Sets:
                if i[0] == a:
                    if j[0] == b:
                        self.Sets.remove(i)
                        self.Sets.remove(j)
                        c = set(i+j)
        self.Sets.append(sorted(c))
S = Partition([(0,3),(0,1),(1,3),(1,0)])
print(S.Sets)
print(S)
S.Union((1,3),(0,1))
S.Union((0,3),(0,1))
print(S)
S.FindSet((1,3))
S.MakeSet((300,1))
S.Union((300,1),(0,1))
print(S)
S.FindSet((300,1))
S.MakeSet((0,0))
S.Union((0,0),(0,1))
S.FindSet((300,1))
print(S)       
