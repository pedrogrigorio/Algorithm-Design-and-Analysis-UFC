value = 0
coin = []

value = int(input("Value to be exchanged: "))
n = int(input("Number of coins: "))

for i in range(n):
    num = int(input("Enter coin value: "))
    coin.append(num)

memo = [[-1 for i in range(value+1)] for j in range(n)]

def change(index_coin, val):
    if(val == 0):
        return 0
    if(index_coin == n and val > 0):
        return float('inf')
    if(val < 0):
        return float('inf')
    if(memo[index_coin][val] == -1):
        memo[index_coin][val] = min(1 + change(index_coin, val-coin[index_coin]), change(index_coin+1, val))
    return memo[index_coin][val]

result = change(0, value)
print("The minimum amount of coins to exchange the values is:", result)