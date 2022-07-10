def skate(S, M, stop, km):
    if(km == 0):
        S[stop][km] = 0
    elif(stop == 0 and km <= d):
        S[stop][km] = 0
    elif(stop == 0 and km > d):
        S[stop][km] = float('inf')
    elif(km - M[stop-1] > d):
        S[stop][km] = float('inf')
    elif(km - M[stop-1] <= d):
        S[stop][km] = min(1 + skate(S, M, stop-1, km-(km-M[stop-1])), skate(S, M, stop-1, km))
    else:
        S[stop][km] = S[stop-1][km]
    return S[stop][km]

km_total = int(input("Total distance in km: "))
d = int(input("How many km without refueling: "))
num_stop = int(input("Number of stops: "))

map = []
for i in range(num_stop):
    num = int(input("Enter stop km: "))
    map.append(num)

S = [[0 for i in range(km_total+1)] for j in range(num_stop+1)]

result = skate(S, map, num_stop, km_total)
print(result)
