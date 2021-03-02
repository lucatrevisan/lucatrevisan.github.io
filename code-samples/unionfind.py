class UnionFind:

    def __init__ (self,V):
        #initializes data structure
        #with elements of list V
        self.rank = { v : 0 for v in V}
        self.parent = { v : v for v in V}
        
    def find(self,x):
        # returns root of tree of x
        while self.parent[x] != x:
            x = self.parent[x]
        return x
        
    def union(self,x,y):
        # merges set of x and set of y
        rtx = self.find(x)
        rty = self.find(y)
        if self.rank[rtx] > self.rank[rty]:
            self.parent[rty] = rtx
        else:
            self.parent[rtx] = rty
            if self.rank[rtx]==self.rank[rty]:
                self.rank[rty] = self.rank[rty]+1
