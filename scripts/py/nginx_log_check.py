#!/usr/bin/python

import os
#import sys
import datetime
import argparse

times = datetime.datetime.now()
str_time = (times - datetime.timedelta(minutes=5)).strftime('/%d\/%b\/%Y:%H:%M/')
end_time = times.strftime('/%d\/%b\/%Y:%H:%M/p')
#print str_time
#print end_time

check_command = 'sed -n "%s,%s"' % (str_time,end_time)
#print check_command

teacherfile = '/var/log/nginx/access_teacherportal.log'
managefile = '/var/log/nginx/access_management.log'
wwwfile = '/var/log/nginx/access_www.log'
apimanagefile = '/var/log/nginx/access_api.management.log'

teacherlist = ['/signInAction.json','/signUpAction.json','/createTimeSlot.json']
managelist = ['/user/student/student/','/operation/fireman/lessonList','/operation/fireman2','/leads/student/students','/finance/packOrder/packOrderAudit/','/leads/order/orders']
wwwlist = ['/parent/login','/parent/signup','/parent/book']
apimanagelist = ['/api/service/private/supplier/getOnlineClassRoomURL']

def log_check(put_status,interface):
#    print interface
#    print managelist
    if interface in teacherlist:
        check_file = teacherfile
    elif interface in managelist:
        check_file = managefile
    elif interface in wwwlist:
        check_file = wwwfile
    elif interface in apimanagelist:
        check_file = apimanagefile
    else:
        return 'input error!'

    check_cmd = '%s %s|grep \'%s\'|awk -F"|" \'{print $5}\'|grep %s|wc -l' % (check_command,check_file,interface,put_status)
    status_list = os.popen(check_cmd).read()
    return status_list.replace('\n','')

#    if status_list != []:
#        status_dic = {}
#        for i in status_list:
#            rep = i.replace('\n','')
#            relist = rep.split()
#            status_numbers = relist[1]
#            if int(status_numbers) > 199:
#                status_dic[status_numbers] = relist[0]
#        if status_dic == {}:
#            return "0"
#        return status_dic
#    else:
#
#        return '0'

def arg_form():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s","--status",help="status number",nargs=1)
    parser.add_argument("-i","--api",help="api module",nargs=1)
    args = parser.parse_args()

    put_status = args.status
    put_api = args.api
    if put_status != None and put_api != None:
        perms_status = args.status[0]
        perms_api = args.api[0]
        print log_check(put_status[0],put_api[0])



if __name__ == '__main__':
    arg_form()
