# take in string of runner's times
# times formatted as hh|mm|ss
# need to determine range of times, median of times, average of times
# return string as "Range: hh|mm|ss Average: hh|mm|ss Median: hh|mm|ss"

import time
def stat(strg):
    if strg == "": return ""
    temp = strg.split(", ")
    for i in range(len(temp)):
        time_run = temp[i].split("|")
        temp[i] = time_run
        for x in range(len(time_run)):
            time_run[x] = int(time_run[x])
    for entry in temp:
        hour = entry[0]*3600
        minute = entry[1]*60
        seconds = entry[2]
        temp[temp.index(entry)] = hour + minute + seconds
    temp.sort()
    r = max(temp) - min(temp)
    avg = sum(temp)// len(temp)
    if len(temp) % 2 == 0:
        median = (temp[(len(temp)//2)] + temp[(len(temp)//2) - 1]) / 2
    else:
        median = temp[(len(temp)//2)]
    r = time.strftime('%H|%M|%S', time.gmtime(r))
    avg = time.strftime('%H|%M|%S', time.gmtime(avg))
    median = time.strftime('%H|%M|%S', time.gmtime(median))
    return "Range: " + r + " Average: " + avg + " Median: " + median
