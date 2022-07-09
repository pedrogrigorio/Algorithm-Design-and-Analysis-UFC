#Function returns the smallest number in the vector

def smallest(v, i, k):
    if(i == k):
        return v[i]
    else:

        #Divide
        j = int((i+k)/2)

        #Conquer
        num1 = smallest(v, i, j)
        num2 = smallest(v, j+1, k)

        #Combine
        if(num1 < num2):
            return num1
        else:
            return num2

vector = []
n = int(input("Size of array: "))

for i in range(n):
    num = int(input("Enter elements: "))
    vector.append(num)

m = smallest(vector, 0, n-1)
print("The smallest number in array is:", m)