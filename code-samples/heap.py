class Heap:

    def __init__ (self,n):
        self.max = n            # maximum size
        self.size = 0           # current size
        self.array = [0]*(n+1)  # array[i] has label of i-th element
        self.key = {}           # key[x] has key of element x
        self.index = {}         # index[x] has position of element x
                                # so that index[array[i]] = i
                                # and array[index[x]] = x
                                    
        
    def parent (self,x):
        # returns label of parent of x
        return self.array[ self.index[x] // 2 ]
        
    def is_leaf (self,x):
        return (self.index[x]*2 > self.size)
        
    def smaller_child (self,x):
        ix = self.index[x]
        y = self.array[2*ix]
        if 2*ix+1 > self.size :
            return x
        else :
            z = self.array[2*ix + 1]
            if self.key[y] < self.key[z]:
                return y
            else:
                return z
                

    def switch (self,x,y):
        # switches positions of elements x and y
        ix = self.index[x]
        iy = self.index[y]
        self.index[x] = iy
        self.index[y] = ix
        self.array[iy] = x
        self.array[ix] = y

    def is_empty (self):
        return (self.size==0)


    def remove_min(self):
        min = self.array[1]
        x = self.array[self.size]
        self.switch (min,x)
        self.size= self.size-1
        if self.size > 0:
            while (not self.is_leaf(x)) and (self.key[x] > self.key[self.smaller_child(x)]):
                self.switch(x,self.smaller_child(x))
        return min
        
    def insert(self,x,k):
        self.size=self.size+1
        self.array[self.size]=x
        self.index[x]=self.size
        self.key[x]=k
        while (self.index[x] >1) and (self.key[x]< self.key[self.parent(x)]):
            self.switch(x,self.parent(x))

        
    def decrease_key(self,x,k):
        self.key[x]=k
        while (self.index[x] >1) and (self.key[x]< self.key[self.parent(x)]):
            self.switch(x,self.parent(x))

        
        
        
