[root@ip-10-0-3-101 bin]# cat run.sh
#!/bin/bash

CATALINA_BASE=$(dirname $0)
CATALINA_BASE=$(cd "$CATALINA_BASE/.."; pwd)

CATALINA_HOME="/opt/tomcat"
export CATALINA_BASE CATALINA_HOME

if ! [ -e $CATALINA_BASE/conf/server.xml ]
then
    echo -e " does not exist $CATALINA_BASE/conf/server.xml\n"
    exit 1;
fi

case "$1" in
    start)
        sh $CATALINA_HOME/bin/startup.sh
        ;;
    stop)
        sh $CATALINA_HOME/bin/shutdown.sh
	;;
    *)
        echo $"Usage: $0 {start|stop}"
        exit 2
esac
exit $?
