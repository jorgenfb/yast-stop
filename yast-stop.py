#!/usr/bin/python

# Add yastlibs to system path to enable importing it later
import sys, os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/yastlibs/python")

from time import time
from argparse import ArgumentParser
from yastlib import *

def stopRecords(yast):
    """Search for all work records in the past 24 hours and stop them"""

    # Define search options to be in the last 24 hours and only 'work'-records
    options = {}
    options['timeFrom'] = int(time()) - 24 * 60 * 60
    options['type'] = 1

    records = yast.getRecords(options).values()

    if not records:
        print('No running records found!')


    for r in records:
        if r.variables['isRunning'] == 1:
            r.variables['isRunning'] = 0;
            r.variables['endTime'] = int(time())
            yast.change(r)
            print('Stopped record ' + str(r.id) + ': ' + r.variables['comment'])

def main():
    parser = ArgumentParser('Stop running tasks started today')
    parser.add_argument('-u', '--user', dest='user', help='username', required=True)
    parser.add_argument('-p', '--password', type=str, dest='password', help='Password for login')
    parser.add_argument('-x', '--hash', dest='hash', help='hash value from yast')
    args = parser.parse_args()

    yast = Yast()

    if args.hash is not None:
        # Username and hash provided. Already logged in
        yast.user = args.user
        yast.hash = args.hash
    elif args.password is not None:
        # Do login
        yast.login(args.user, args.password)
    else:
        # Neither hash or password defined abort
        raise Exception('Neither hash or password provided. Please provide one of them.')

    stopRecords(yast)


if __name__ == '__main__':
    main();
