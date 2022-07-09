#Function returns the index of the number searched for in a sorted array.

def binarySearch(v, i, k, target):

    j = int((i + k)/2)

    if(i > k):
        return -1
    elif(v[j] == target):
        return j
    elif(target > v[j]):
        index = binarySearch(v, j+1, k, target)
        return index
    else:
        index = binarySearch(v, i, j-1, target)
        return index

vector = []
n = int(input("Size of array: "))

for i in range(n):
    num = int(input("Enter elements: "))
    vector.append(num)

target = int(input("Number searched for: "))

index = binarySearch(vector, 0, n-1, target)
print("Number index:", index)
