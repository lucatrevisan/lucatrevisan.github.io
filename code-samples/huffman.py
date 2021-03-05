from heap import Heap

class HuffmanTree:

    def __init__ (self,n,f):
    
        self.left = [None]*(2*n-1)
        self.right = [None]*(2*n-1)
        self.first_available = n
        self.root = 2*n-2
        self.n = n
        self.intdecode = []
        self.f =f
        
    def add_internal (self,a,b):
    
        v = self.first_available
        self.first_available = self.first_available + 1
        self.left[v]=a
        self.right[v]=b
        return v
        
        
    def encodings (self):
    
        stack = [self.root]
        L = [""]*(self.root+1)
        while stack:
            v = stack.pop()
            if v >= self.n:
                rightchild = self.right[v]
                leftchild = self.left[v]
                L[rightchild] = L[v] + "1"
                stack.append(rightchild)
                leftchild = self.left[v]
                L[leftchild]= L [v] + "0"
                stack.append(leftchild)
        return L
        

    def parse (self,s):
    
        P=[]
        v = self.root
        for i in range(len(s)):
            if s[i]=="0":
                v = self.left[v]
            else:
                v = self.right[v]
            if v < self.n :
                P = P + [v]
                v = self.root
        return P
        

def encode_list (T,L):

    enc = ""
    E = T.encodings()
    for v in L:
        enc = enc+E[v]
    return enc
        
def encode(s):

    chartoint = {}
    inttochar = []
    n=0
    f=[]
    source = []
    for i in range(len(s)):
        if s[i] not in chartoint:
            chartoint[s[i]]=n
            inttochar.append(s[i])
            f.append(0)
            n=n+1
        source.append(chartoint[s[i]])
        f[chartoint[s[i]]] = f[chartoint[s[i]]] + 1
    
    T = huffman(f,n)
    T.intdecode = inttochar
    enc = encode_list(T,source)
    return T,enc

def decode(T,enc):
    declist = T.parse(enc)
    decstring = ""
    for i in range(len(declist)):
        decstring = decstring + T.intdecode[declist[i]]
    return decstring



def huffman (f,n):

    Q = Heap(n)
    T = HuffmanTree(n,f)
    F = [0]*(2*n-1)
    for v in range(n):
        Q.insert(v,f[v])
        F[v] = f[v]
    for i in range(n-1):
        a = Q.remove_min()
        b = Q.remove_min()
        v = T.add_internal(a,b)
        F[v] = F[a]+F[b]
        Q.insert(v,F[v])
    return T
        



with open('costituzione.txt', 'r') as file:
    s = file.read()

T,enc = encode(s)
decs = decode(T,enc)

E= T.encodings()
report = [ (v,T.intdecode[v],T.f[v],E[v]) for v in range(T.n)]
report.sort(key = lambda x : x[2])
for row in report:
    print(row[1]+" "+str(row[2])+" "+row[3])

if decs==s:
    print("worked")
    print("length of file "+str(len(s))+" characters")
    print("length of compression "+str(len(enc))+" bits")


