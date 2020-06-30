def nbMonths(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth):
    count = 0
    total_saved = 0
    rate = 10**(-2)*percentLossByMonth*count
    price_old = startPriceOld * (1 - (rate * count)) + total_saved
    price_new = startPriceNew * (1 - (rate * count))
    while (price_old + savingperMonth*count) < price_new:
        total_saved = savingperMonth * count
        if count % 2 == 0:
            rate = rate_increase(count // 2, percentLossByMonth)
        test_price = price_old - (price_old * percentLossByMonth/100)
        price_old -= (price_old * percentLossByMonth/100)
        price_new -= (price_new * percentLossByMonth/100)
        new_total = price_old + total_saved
        print(price_new)
        print(total_saved + price_old)
        count += 1
    return [count,((price_old + total_saved) - price_new)]
def rate_increase(n, percentPerMonth):
    rate = 10**(-2)*(percentPerMonth + (0.5*n))
    return rate
    
