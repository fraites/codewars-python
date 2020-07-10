# have to take exactly ten minutes
# one direction = one minute
# must end up where you started

# works for all basic tests, failing some of the random tests

def is_valid_walk(walk):
    dict = {}
    sum = 0
    if len(walk) != 10:
        return False
    for d in walk:
        if d in dict.keys():
            dict[d] += 1
        else:
            dict[d] = 1
    if 'n' in dict.keys() and 's' in dict.keys():
        return dict['n'] == dict['s']
    elif 'w' in dict.keys() and 'e' in dict.keys():
        return dict['w'] == dict['e']
    elif 'n' in dict.keys() and 's' in dict.keys() and 'w' in dict.keys() and 'e' in dict.keys():
        return dict['n'] == dict['s'] and dict['w'] == dict['e']
    else: return False
