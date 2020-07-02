def up_array(arr):
    if not arr: return None
    for x in arr:
        if not (0 <= x < 10):
            return None
    temp = map(str,arr)
    temp = int(''.join(temp)) + 1
    return list(map(int,str(temp)))
