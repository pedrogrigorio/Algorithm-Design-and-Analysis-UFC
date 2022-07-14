def pedagio(X,R,S,i,m):
    if(i==0 or m == 0):
        S[i][m] = 0
    elif m < 0:
        return 0
    elif m > X[i-1]:
        S[i][m] = max(pedagio(X,R,S,i,m-1), pedagio(X,R,S,i-1,m))
    elif m == X[i-1]:
        S[i][m] = max(pedagio(X,R,S,i-1,m-5)+R[i-1], pedagio(X,R,S,i-1,m))
    else:
        S[i][m] = pedagio(X,R,S,i-1,m)
    return S[i][m]


M = int(input("Road length: "))
n = int(input("Number of tolls: "))
X = []
R = []
for i in range(n):
    km = int(input("Toll mileage: "))
    X.append(km)

for i in range(n):
    value = int(input("Toll values: "))
    R.append(value)

S = [[0 for j in range(M+1)] for i in range(len(X)+1)]

result = pedagio(X,R,S,len(X),M)
print("Maximum gain is:",result)