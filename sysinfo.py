from flask import Flask

from lib import network
from lib import ubuntu

print('sysinfo')

dict_rute = network.gaseste_rutele()
dict_linkuri = network.gaseste_linkuri()
dict_adrese = network.gaseste_adrese()

rute = network.genereaza_tabela_rute(dict_rute)

v_ub = ubuntu.gaseste_versiune_ubuntu()
mem = ubuntu.gaseste_informatii_memorie()
cpu = ubuntu.gaseste_informatii_cpu()

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    ret = "<pre>"
    ret += "Informatii despre sistemul de operare pe care ruleaza aplicatia:\n"
    ret += "\nVersiune UBUNTU:\n"
    ret += "\n" + v_ub + "\n"
    ret += "\nMEMORIE\n" + mem + "\n"
    ret += "\nNuclee CPU:\n" + cpu + "\n"
    
    ret += "\n\n\n"
    ret += "Informatii despre retea:\n"
    ret += "\nRUTE:\n" + str(rute) + "\n"
    
    ret += "\nAdrese IP:\n" + str(dict_adrese) + "\n"
    
    ret += "</pre>"
    
    return ret
    
@app.route("/vos", methods=['GET'])
def versiune_os():
    ret = "<pre>"
    ret += v_ub
    ret += "</pre>"
    return ret
    
@app.route("/mem", methods=['GET'])
def info_memorie():
    ret = "<pre>"
    ret += mem
    ret += "</pre>"
    return ret
    
@app.route("/cpu", methods=['GET'])
def info_cpu():
    ret = "<pre>"
    ret += cpu
    ret += "</pre>"
    return ret
