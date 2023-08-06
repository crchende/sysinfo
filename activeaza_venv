# venv-ul se gaseste in directorul parinte: .venv
# source ../.venv/bin/activate
. .venv/bin/activate

# daca comanda de mai sus esueaza, creaza .venv si instaleaza dependintele
# venv-ul va ramane activat in acest caz
if [ $? -eq 0 ]
then
    echo "SUCCESS: venv was activated."
else
    echo "FAIL: cannot activate venv"
    . ./activeaza_venv_jenkins
fi
