#!/bin/bash

currentDate=`date +%Y%m%d`
currentDir=/usr/local/bin/slow_interface

cat /var/log/nginx/access_www.log |awk '{if($(NF-4)>3)print $(NF-4), $7}'|awk -F'?|;' '{print $1}'| awk '{max[$2]=max[$2]>$1?max[$2]:$1;number[$2]++;sum
[$2]+=$1} END{for (i in max) print max[i], sum[i]/number[i],number[i],i}'|sort -nr > ${currentDir}/temp.txt
