def nbMonths(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth):
    count = 0
    total_saved = 0
    rate = 10**(-2)*percentLossByMonth*count
    price_old = startPriceOld * (1 - (rate * count)) + total_saved
    price_new = startPriceNew * (1 - (rate * count))
    # this loop has the right idea, but doesnt work as planned
    while (price_old + savingperMonth*count) < price_new:
        total_saved = savingperMonth * count
        if count % 2 == 0:
            # successfully increases the rate by 0.5 every 2 months
            rate += 0.5
        test_price = price_old - (price_old * percentLossByMonth/100)
        price_old -= (price_old * percentLossByMonth/100)
        price_new -= (price_new * percentLossByMonth/100)
        new_total = price_old + total_saved
        print(price_new)
        print(total_saved + price_old)
        count += 1
    # this only works for test case where old > new already
    return [count,((price_old + total_saved) - price_new)]

# custom function used to increase rate based on variable % per month
def rate_increase(n, percentPerMonth):
    rate = 10**(-2)*(percentPerMonth + (0.5*n))
    return rate
   
