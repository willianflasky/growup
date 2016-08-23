#!/usr/bin/python
import os,sys
import logging

logging.basicConfig(level=logging.DEBUG,
                format="%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s",
                datefmt="%a,%d %b %Y %H:%M:%S",
                filename="/tmp/restart_appsever.log",
                filemode='a')


def main():
	cmd="uptime |awk '{print $11}' |awk -F',' '{print $1}'"
	loadValue=os.popen(cmd).read()
	if loadValue > '2':
	    ret=os.system('/etc/init.d/appserver restart')
	    if ret == 0:
	        logging.info("restart ok.")
	    else:
	        logging.warning("restart error.")
	else:
	    logging.info('load value=%s'%loadValue)


if __name__ == "__main__":
	main()
