def smallestDifference(v, i, k):
    if(k-i == 0):
        return v[k]
    elif(k-i == 1):
        return (v[k]-v[i])
    else:
        j = int((i+k)/2)

        l = smallestDifference(v, i, j)
        m = smallestDifference(v, j, j+1)
        r = smallestDifference(v, j+1, k)

        if(l <= m) and (l <= r):
            return l
        elif(m <= l) and (m <= r):
            return m
        else:
            return r


vector = []
n = int(input("Size of array: "))

for i in range(n):
    num= int(input("Enter elements: "))
    vector.append(num)

result = smallestDifference(vector, 0, n-1)
print(result)