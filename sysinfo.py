from flask import Flask, url_for

from app.lib import network
from app.lib import ubuntu

print('sysinfo')

dict_rute = network.gaseste_rutele()
dict_linkuri = network.gaseste_linkuri()
dict_adrese = network.gaseste_adrese()

rute_scurt = network.genereaza_tabela_rute(dict_rute)

v_ub = ubuntu.gaseste_versiune_ubuntu()
mem = ubuntu.gaseste_informatii_memorie()
cpu = ubuntu.gaseste_informatii_cpu()

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    ret = ""
    ret += f"[<a href={url_for('versiune_os')}>Doar Versiunea Sistemului de operare</a>] "
    ret += f"[<a href={url_for('info_memorie')}>Doar Memoria</a>] "
    ret += f"[<a href={url_for('info_cpu')}>Doar procesorul</a>] <br>"

    ret += f"[<a href={url_for('info_retea_rute')}>Info retea: rute</a>] "
    ret += f"[<a href={url_for('info_retea_rute_full')}>Info retea: rute (full)</a>] "
    ret += f"[<a href={url_for('info_retea_adrese')}>Info retea: adrese</a>] <br>"

    ret += "<pre>"
    ret += "Informatii despre sistemul de operare pe care ruleaza aplicatia:\n"
    ret += "\nVersiune UBUNTU:\n"
    ret += "\n" + v_ub + "\n"
    ret += "\nMEMORIE\n" + mem + "\n"
    ret += "\nNuclee CPU:\n" + cpu + "\n"
    
    ret += "\n\n\n"
    ret += "Informatii despre retea:\n"
    ret += "\nRUTE:\n" + str(rute_scurt) + "\n"
    
    ret += "\nAdrese IP:\n" + str(dict_adrese) + "\n"
    
    ret += "</pre>"
    
    return ret
    
@app.route("/vos", methods=['GET'])
def versiune_os():
    ret = ""
    ret += f"<a href={url_for('index')}>acasa</a>"
    ret += "<pre>"
    ret += v_ub
    ret += "</pre>"
    return ret
    
@app.route("/mem", methods=['GET'])
def info_memorie():
    ret = ""
    ret += f"<a href={url_for('index')}>acasa</a>"
    ret += "<pre>"
    ret += mem
    ret += "</pre>"
    return ret
    
@app.route("/cpu", methods=['GET'])
def info_cpu():
    ret = ""
    ret += f"<a href={url_for('index')}>acasa</a>"
    ret += "<pre>"
    ret += cpu
    ret += "</pre>"
    return ret

@app.route("/retea/rute", methods=['GET'])
def info_retea_rute():
    ret = ""
    ret += f"<a href={url_for('index')}>acasa</a>"
    ret += "<pre>"
    ret += str(rute_scurt)
    ret += "</pre>"
    return ret

@app.route("/retea/rute_full", methods=['GET'])
def info_retea_rute_full():
    ret = ""
    ret += f"<a href={url_for('index')}>acasa</a>"
    ret += "<pre>"
    ret += str(dict_rute)
    ret += "</pre>"
    return ret

@app.route("/retea/interfete", methods=['GET'])
def info_retea_adrese():
    ret = ""
    ret += f"<a href={url_for('index')}>acasa</a>"
    ret += "<pre>"
    ret += str(dict_adrese)
    ret += "</pre>"
    return ret