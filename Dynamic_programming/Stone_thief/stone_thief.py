def steal(R, S, h, w, i, j):
    if(S[i][j] != 0):
        S[i][j] = S[i][j]
    elif(i == h-1):
        S[i][j] = R[i][j]
    elif(j == 0):
        S[i][j] = max(R[i][j] + steal(R, S, h, w, i+1,j), R[i][j] + steal(R, S, h, w, i+1,j+1))
    elif(j == w-1):
        S[i][j] = max(R[i][j] + steal(R, S, h, w, i+1,j), R[i][j] + steal(R, S, h, w, i+1,j-1))
    else:
        S[i][j] = max(R[i][j] + steal(R, S, h, w, i+1,j-1), R[i][j] + steal(R, S, h, w, i+1,j), R[i][j] + steal(R, S, h, w, i+1,j+1))
    if(i == 0 and j != w-1):
        return max(S[i][j], steal(R,S, h, w, i,j+1))
    return S[i][j]

h = int(input("Number of rows: "))
w = int(input("Number of columns: "))
room = [[0 for i in range(w)] for j in range(h)]
for i in range(h):
    for j in range(w):
        room[i][j] = int(input("Amount of stones: "))

S = [[0 for i in range(w)] for j in range(h)]
result = steal(room, S, h, w, 0, 0)
print("The maximum of stones she can get is:",result)