# works for most cases, except case where there is inner solution
# example ([5,3,7,5], 10) returns [5,5] when [3,7] is solution
def sum_pairs(ints, s):
    for i in range(0,len(ints)):
        for j in range(i+1,len(ints)):
            if ints[i] + ints[j] == s:
                return [ints[i],ints[j]]
    return None
