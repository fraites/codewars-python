# took another approach to use $ type as key & quantity as value
def tickets(people):
    # dict object to represent payment to cashier
    register = {100:0,50:0,25:0}
    for pay in people:
        if pay == 25:
            register[25] += 1
        elif pay == 50:
            if register[25] == 0:
                return 'NO'
            register[50] += 1
            register[25] -= 1
        else:
            register[100] += 1
            if register[50] >= 1 and register[25] >= 1:
                register[50] -= 1
                register[25] -= 1
            elif register[25] >= 3:
                register[25] -= 3
            else:
                return 'NO'
    return 'YES'
