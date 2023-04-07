#!/bin/sh
echo "changing directory to app:"
cd ./app
echo "Activare venv:"
#source ../.vanv/bin/activate
. ../.venv/bin/activate
echo "Configurare variabila mediu FLASK_APP"
export FLASK_APP=sysinfo
echo "Start server:"
exec flask run -h 0.0.0.0 -p 5020 --reload
