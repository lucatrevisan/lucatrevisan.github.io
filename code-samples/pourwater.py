max = [4,7,10]
n = 3


def pour(S,i,j):

    # pours from bin i to bin j
    
    T =  [ S[i] for i in range(n)]

    if S[i] + S[j] <= max[j]:
        newi = 0
        newj = S[i] + S[j]
    else :
        newj = max[j]
        newi = S[i]+ S[j]-newj
    T[i] = newi
    T[j] = newj
    return T
    
def BFS(S):
    prev = {}
    visited = {tuple(S)}
    Q = [tuple(S)]
    while  Q:
        V = list(Q.pop(0))
        for i in range(n):
            for j in range(n):
                W = pour(V,i,j)
                if tuple(W) not in visited:
                    visited.add(tuple(W))
                    Q = Q + [tuple(W)]
                    prev [tuple(W)] = tuple(V)
    return visited, prev
    
def find_strategy(initial,goal):
    visited,prev = BFS(initial)
    if tuple(goal) not in visited :
        return []
    else :
        p = tuple(goal)
        L = [p]
        while p!= tuple(initial):
            p = prev[p]
            L = [p]+L
        return L

                
