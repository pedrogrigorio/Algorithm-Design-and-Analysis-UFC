#Function returns the index of the greatest number in the array

def greatest(v, i, k):
    if(i == k):
        return i
    else:
        #Divide
        j = int((i+k)/2)

        #Conquer
        l = greatest(v, i, j)
        r = greatest(v, i+1, k)

        #Combine
        if(v[l] > v[r]):
            return l
        else:
            return r

vector = []
n = int(input("Size of array: "))

for i in range(n):
    num = int(input("Enter elements: "))
    vector.append(num)

gr = greatest(vector, 0, n-1)
print("The index of the greatest number is:", gr)
