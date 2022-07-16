def box(A, n, H):
    C = []
    C.append(A[0])
    for i in range(1,n,1):
        notFit = True
        for k in range(len(C)):
            if (A[i] + C[k] <= H):
                C[k] = C[k] + A[i]
                notFit = False
                break
        if(notFit):
            C.append(A[i])
    return len(C)

n = int(input("Number of objects: "))
H = int(input("Enter the boxes height: "))
A = []
for i in range(n):
    num = int(input("Enter objects heights in non-ascending order: "))
    A.append(num)
result = box(A, n, H)
print("The minimum of boxes is: ", result)