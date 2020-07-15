# purpose is to find the 'stationary number'
# stationary number = number that will be the same regardless how many times it goes through loop
# div_13 sequence: [1, 10, 9, 12, 3, 4]
# eventually recursive calls should yield n = total = stationary number

def thirt(n):
    total = 0
    a = [int(x) for x in str(n)]
    a.reverse()
    for i in range(len(a)):
        div_13 = (10**i) % 13
        total += a[i]*div_13
    if total != n:
        return thirt(total)
    else:
        return total
        
