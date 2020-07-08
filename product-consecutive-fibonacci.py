# Given a number, say prod (for product), we search two Fibonacci numbers F(n) and F(n+1) verifying
# F(n) * F(n+1) = prod.
# Your function productFib takes an integer (prod) and returns an array:
# [F(n), F(n+1), true] or {F(n), F(n+1), 1} or (F(n), F(n+1), True)
# depending on the language if F(n) * F(n+1) = prod.
# If you don't find two consecutive F(m) verifying F(m) * F(m+1) = prodyou will return
# [F(m), F(m+1), false] or {F(n), F(n+1), 0} or (F(n), F(n+1), False)
# F(m) being the smallest one such as F(m) * F(m+1) > prod.

# My first solution
def productFib(prod):
    x = 0
    y = x + 1
    while (x*y < prod):
        temp = x
        x = y
        y = temp + x
    return [x, y, (x*y == prod)]

# another possible solution
def productFib(prod):
    x, y = 0, 1
    while (x*y < prod):
        x, y = y, x+y
    return [x,y,(x*y == prod)]
 
