#!/usr/bin/env python
#decoding=utf8
import os
import sys
import logging

BASE_DIR=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASE_DIR)
from hashlib import md5
from myftp.conf import settings
from pyftpdlib.handlers import FTPHandler,ThrottledDTPHandler
from pyftpdlib.authorizers import DummyAuthorizer,AuthenticationFailed
from pyftpdlib.servers import FTPServer
from pyftpdlib.filesystems import UnixFilesystem
from pyftpdlib.authorizers import UnixAuthorizer
from pyftpdlib.servers import MultiprocessFTPServer
from myftp.modules import auth

def main():
    authorizer = DummyAuthorizer()
    authorizer.add_user('admin','123456',os.getcwd(),perm='elradfmw')
 
    for user in auth.data:
        s1=user.split('=')[1]
        ret=s1.split(',')
        authorizer.add_user(ret[0].replace("'",""),ret[1],os.getcwd(),perm=ret[2].strip().replace("'",""))

    #aauthorizer.add_anonymous(os.getcwd())
    dtp_handler = ThrottledDTPHandler
    dtp_handler.read_limit=30720
    dtp_handler.write_limit=30720

    handler = FTPHandler
    handler.authorizer = authorizer
    handler.dtp_handler=dtp_handler
    logging.basicConfig(filename='%s/myftp/logs/pyftpd.log'%BASE_DIR,level=settings.level)

    handler.banner = 'pyftpdlib based ftpd ready'

    address=('',2121)
    server=MultiprocessFTPServer(address,handler)

    server.max_conns=settings.maxconn
    server.max_conns_pre_ip=settings.maxconnperip
    
    server.serve_forever()

if __name__ == '__main__':
    main()
