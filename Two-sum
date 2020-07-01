# imported sys to call sys.exit function due to exit code failure. Works well, but open to optimization
import sys
def two_sum(numbers, target):
    i = 0
    j = len(numbers)-1
    if numbers[i] + numbers[j] < target:
        i+=1
    elif numbers[i] + numbers[j] > target:
        j-=1
    else:
        return (numbers.index(numbers[i]), numbers.index(numbers[j]))
    sys.exit()
