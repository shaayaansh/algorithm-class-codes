input_array = input("Please Enter the price for each length of rod, with space between numbers : \n")
prices = input_array.split(" ")
for i in range(len(prices)):
    prices[i] = int(prices[i])

INT_MIN = -32767


def cut_rod(price_array, n):
    revenue = [0 for x in range(n+1)]
    revenue[0] = 0

    for i in range(1, n+1):
        q = INT_MIN
        for j in range(i):
            q = max(q, prices[j] + revenue[i-j-1])
        revenue[i] = q
    return revenue[n]


print("MAXIMUM OBTAINABLE REVENUE IS : ", cut_rod(prices, len(prices)))
