#X = ['B', 'A', 'C', 'B', 'A', 'D']
#Y = ['A', 'B', 'A', 'Z', 'D', 'C']

def LCS(S,X,Y,i,j):
    if(i == 0 or j == 0):
        S[i][j] = 0
    elif(X[i-1] == Y[j-1]):
        S[i][j] = LCS(S,X,Y,i-1,j-1) + 1
    else:
        S[i][j] = max(LCS(S,X,Y,i, j-1), LCS(S,X,Y,i-1,j))
    return S[i][j]

X = []
Y = []
X_lenght = int(input("Enter size of first array: "))
Y_lenght = int(input("Enter size of first array: "))

for i in range(X_lenght):
    str = input("Enter first string: ")
    X.append(str)
X

for i in range(Y_lenght):
    str = input("Enter second string: ")
    Y.append(str)

S = [[0 for j in range(Y_lenght+1)] for i in range(X_lenght+1)]

result = LCS(S,X,Y,X_lenght,Y_lenght)
print("The longest common subsequence in strings has length:", result)
