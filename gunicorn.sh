#!/bin/bash
set -e
LOGFILE=log/gunicorn/hello.log
LOGDIR=$(dirname $LOGFILE)
NUM_WORKERS=3
# user/group to run as
USER=bibi
GROUP=your_unix_group
cd ~/findburo/findburo
source ../bin/activate
test -d $LOGDIR || mkdir -p $LOGDIR
exec ../bin/gunicorn_django -w $NUM_WORKERS \
    --user=$USER --log-level=debug \
    --log-file=$LOGFILE 2>>$LOGFILE
