#!/bin/sh
echo "Activare venv:"
#source .vanv/bin/activate
. .venv/bin/activate
echo "Configurare variabila mediu FLASK_APP"
export FLASK_APP=sysinfo
cale=`pwd`
echo "CALE: " $x
lsdir=`ls -1`
echo "CONTINUT DIRECTOR: " $lsdir
echo "Start server:"
exec flask run -h 0.0.0.0 -p 5011 --reload
