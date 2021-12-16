#!/usr/bin/python3
""" a script that reads stdin line by line and computes metrics: """
import sys


i = 0
val = ""
totalsize = 0
status = [200, 301, 400, 401, 403, 404, 405, 500]
dict = {200: 0, 301: 0, 400: 0, 401: 0,
        403: 0, 404: 0, 405: 0, 500: 0}


def printstatus(dict, totalsize):
    """print status"""
    print("File size: {}".format(totalsize))
    for item in status:
        if dict[item]:
            print("{}: {}".format(item, dict[item]))


try:
    for val in sys.stdin:
        i += 1
        mylist = val.split()
        if len(mylist) == 9:
            try:
                totalsize += int(mylist[-1])
            except Exception:
                pass
            try:
                stat = int(mylist[-2])
            except Exception:
                pass
            if stat in status:
                dict[stat] += 1
        if i % 10 == 0:
            printstatus(dict, totalsize)
except KeyboardInterrupt:
    pass
finally:
    printstatus(dict, totalsize)
