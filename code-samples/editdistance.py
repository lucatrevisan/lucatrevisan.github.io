def edit_distance(a,b):

    n = len(a)
    m = len(b)
    D = [[0 for j in range (-1,m)] for i in range(-1,n) ]
    D[-1][-1]=0

    for i in range(n):
        D[i][-1] = i+1
    for j in range(m):
        D[-1][j] = j+1
    for j in range(m):
        for i in range(n):
            D[i][j] = min (
                1 + D[i-1][j],
                1 + D[i][j-1],
                (0 if a[i]==b[j] else 1) + D[i-1][j-1])
    return D[n-1][m-1]

