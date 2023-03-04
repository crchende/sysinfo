import Flask

from lib import network
from lib import ubuntu

print('pytestdemo.py')

rute = network.gaseste_rutele()
linkuri = network.gaseste_linkuri()
adrese = network.gaseste_adrese()

network.genereaza_tabela_rute(rute)

ubuntu.gaseste_versiune_ubuntu()
ubuntu.gaseste_informatii_memorie()
ubuntu.gaseste_informatii_cpu()
