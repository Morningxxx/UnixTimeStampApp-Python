import os
import sys
import random
import time
import datetime
import calendar
import argparse


parser = argparse.ArgumentParser()

parser.add_argument('-u', '--unix', required=None, nargs='?', type=int, help="give now unix stamp", default=-1)
parser.add_argument('-s', '--second', required=None, nargs='?', type=int, help="turn unix stamp to time", default=-1)
parser.add_argument('-d', '--date', required=None, nargs='?', type=int, help="turn date to unixstamp, date should form like 'yyyyMMddhhmmss'", default=0)

args = parser.parse_args()
unix = args.unix
sec = args.second


def main():
    if unix != -1:
        ts = int(time.mktime(datetime.datetime.now().utctimetuple()))
        print(ts)
        return

    if sec == None:
        # print("'-s' need a following arg with type int")
        now = datetime.datetime.now()
        print now
        return
    else:
        if sec >= 0:
            ts = sec
            now = datetime.datetime.utcfromtimestamp(ts)
            print(now)
            return
        # try:
        #     now = datetime.datetime.utcfromtimestamp(ts)
        #     print(now)

    date = args.date
    if date > 0:
        try:
            ss = date % 100
            if ss > 60 or ss < 0:
                print('availd arg')
                return
            date = int(date / 100)

            mm = date % 100
            if mm > 60 or mm < 0:
                print('availd arg')
                return
            date = int(date / 100)

            hh = date % 100
            if hh > 23 or hh < 0:
                print('availd arg')
                return
            date = int(date / 100)

            dd = date % 100
            if dd > 31 or dd < 1:
                print('availd arg')
                return
            date = int(date / 100)

            MM = date % 100
            if MM > 12 or MM < 1:
                print('availd arg')
                return
            date = int(date / 100)

            yyyy = date
            if yyyy > 9999 or yyyy < 0:
                print('availd arg')
                return
        except:
            print('availd arg')
            return
        try:
            newDate = datetime.datetime(yyyy, MM, dd, hh, mm, ss)
            ts = int(time.mktime(newDate.utctimetuple()))
            print(ts)
        except:
            print("can't form date by arg")
        return


main()







