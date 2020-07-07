# works for every test case (including randoms) except one unidentified, even tried using print to diagnose but doesnt apply
import math
def comp(array1, array2):
    if not array1 or not array2:
        return False
    else:
        sorted_1 = [abs(x) for x in array1]
        sorted_2 = []
        for x in array2:
            x = math.sqrt(x)
            sorted_2.append(x)
    return(sorted(sorted_1) == sorted(sorted_2))
	
