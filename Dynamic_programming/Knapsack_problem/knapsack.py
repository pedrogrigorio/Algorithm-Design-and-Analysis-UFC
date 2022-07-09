def knapsack(V, P, i, cap):
    if(cap == 0 or i == 0):
        return 0
    elif(P[i-1] <= cap):
        K[i][cap] = max(V[i-1] + knapsack(V, P, i-1, cap-P[i-1]), knapsack(V, P, i-1, cap))
    else:
        K[i][cap] = K[i-1][cap]
    return K[i][cap]

capacity = int(input("Size of knapsack: "))
items = int(input("Number of items: "))
V = []
W = []
K = []

for i in range(items):
    num = int(input("Enter item values: "))
    V.append(num)

for i in range(items):
    num = int(input("Enter item weights: "))
    W.append(num)


K = [[0 for i in range(capacity+1)] for j in range(items+1)]

result = knapsack(V, W, items, capacity)
print("The maximum possible value in the knapsack is:", result)