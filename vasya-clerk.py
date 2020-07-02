# this function works for 18/20 cases
# need to determine point for failures
def tickets(people):
    # array variable to use as register
    register = []
    # cost of ticket
    cost = 25
    # variable to hold change needed to return
    change = 0
    index_25 = 0
    index_50 = 0
    # go through each x in people
    # add payment to new array to use as register
    for x in people:
        # add payment to register
        register.append(x)
        # determine if they paid more than cost
        if x > cost:
            change = x - cost
            # determines how much change to give back
            if change == 75:
                if 25 not in register or 50 not in register:
                    return "NO"
                else:
                    index_25 = register.index(25)
                    index_50 = register.index(50)
                    del register[index_25]
                    del register[index_50]
            else:
                if 25 not in register:
                    return "NO"
                else:
                    index_25 = register.index(25)
                    del register[index_25]
    return "YES"
