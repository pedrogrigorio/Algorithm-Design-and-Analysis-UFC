def antenna(H):
    S = []
    S.append(H[0] + 4)
    k = 0
    for i in range(len(H)-1):
        i = i + 1
        if(abs(H[i] - S[k]) > 4):
            S.append(H[i] + 4)
            k = k + 1
    return S

n = int(input("Number of houses: "))
H = []
for i in range(n):
    km = int(input("Enter house mileage: "))
    H.append(km) 

S = antenna(H)
print("Antennas in the following locations: ",S)