# you have either all even array or all odd array & need to find even or odd outlier, respectively
# Test Cases:
# test.assert_equals(find_outlier([2, 4, 6, 8, 10, 3]), 3)
# test.assert_equals(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]), 11)
# test.assert_equals(find_outlier([160, 3, 1719, 19, 11, 13, -21]), 160)

def find_outlier(integers):
    odd = [x for x in integers if x%2!=0]
    even = [x for x in integers if x%2==0]
    if len(even) > len(odd): return odd[0]
    else: return even[0]
