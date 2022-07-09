def smallest(v, n):
    if(n==1):
        return v[0]
    else:
        m = smallest(v, n-1)
        if(m < v[n-1]):
            return m
        else:
            return v[n-1]

vector = []
n = int(input("Vector length: "))

for i in range(n):
    num= int(input("Enter elements: "))
    vector.append(num)

m = smallest(vector, n)
print(m)