#!/usr/bin/env python
"""
2016-05-04
monit 8080
"""

import argparse
import requests
parser=argparse.ArgumentParser()
parser.add_argument("-i","--ip",default="127.0.0.1:8080",help="eg: 10.0.1.1:8080",type=str)
args=parser.parse_args()

def monitorPort(ipport):
    try:
        url = 'http://{0}'.format(ipport)
        r = requests.get(url)
        print r.status_code
    except requests.exceptions.RequestException as e:
        print 0

monitorPort(args.ip)
