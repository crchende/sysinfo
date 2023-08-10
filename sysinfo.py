from flask import Flask, url_for

from app.lib import network
from app.lib import ubuntu
from app.grafice.exemplu_func_grad_2 import valori_x, valori_y, genereaza_grafice

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

    ret += "\n\nExemplu reprezentare grafica - functie de grad 2: y = x*x.\n"
    ret += "Graficul este doar pentru a exemplifica o metoda de afisare grafica\n"
    ret += "Folosind metoda prezentata, se pot afisa grafice referitoare la sitemul de operare cum ar fi:\n"
    ret += " - graficul de utiliare a memoriei in timp, a procesorului etc"
    ret += "Link: <a href=" + url_for("grafic_x_patrat") + ">Grafice functie grad 2</a>" + "<br/>"
    
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

@app.route("/grafic_x_patrat", methods=['GET'])
def grafic_x_patrat():
    genereaza_grafice(valori_x, valori_y, "static/imagini")
    #t1 = threading.Thread(target=genereaza_grafice, args = (valori_x, valori_y, "static/imagini"))
    #t1.start()
    #t1.join()
    ret = f"<a href={url_for('index')}>acasa</a><br/>"
    
    ret += "valori x: " + str(valori_x) + "<br/>"
    ret += "valori y = x*x: " + str(valori_y) + "<br/>"

    ret += '<br><b>BUG</b><br>'
    ret += 'matplotlib nu functioneaza bine daca nu este utilizat in thread-ul prinicipal<br>'
    ret += 'La primul apel merge dar la urmatoarele apeluri poate strica aplicatia - "crash"'
    ret += 'Vezi sugestia de fix/workaround din README.md<br><br>'
    
    ret += f'<img src={url_for("static", filename="imagini/afisare_cu_punct.png")}>' + "<br/>"
    ret += f'<img src={url_for("static", filename="imagini/afisare_cu_steluta.png")}>' + "<br/>"
    ret += f'<img src={url_for("static", filename="imagini/afisare_cu_x.png")}>' + "<br/>"
    ret += f'<img src={url_for("static", filename="imagini/grafic_continuu_v1.png")}>' + "<br/>"
    ret += f'<img src={url_for("static", filename="imagini/grafic_continuu_v2.png")}>' + "<br/>"
    
    return ret
