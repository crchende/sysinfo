import sys

from flask import Flask, url_for

from app.lib import network
from app.lib import linux
from app.grafice.exemplu_func_grad_2 import valori_x, valori_y, genereaza_grafice

print('sysinfo')

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    ret = "<h1>SYSINFO</h1>"
    ret += "<h3>Varianta simplificata. Codul 'view' (care genereaza paginile web) intr-un singur fisier, fara teamplate-uri, formatare minimala.</h3>"
    
    ret += "Sistem de operare: "
    ret += f"[<a href={url_for('versiune_os')}>Versiune</a>] "
    ret += f"[<a href={url_for('info_memorie')}>Memorie</a>] "
    ret += f"[<a href={url_for('info_cpu')}>Procesor</a>] <br>"

    ret += "Retea: "
    ret += f"[<a href={url_for('info_retea_rute')}>Rute</a>] "
    ret += f"[<a href={url_for('info_retea_adrese')}>Adrese</a>] <br>"

    ret += "<pre>"
    ret += "Informatii despre sistemul de operare pe care ruleaza aplicatia:\n"
    ret += "\nVersiune linux:\n"
    ret += "\n" + linux.gaseste_versiune_linux() + "\n"
    ret += "\nMEMORIE\n" + linux.gaseste_informatii_memorie(formatare = 1) + "\n"
    ret += "\nNuclee CPU:\n" + linux.gaseste_informatii_cpu() + "\n"
    
    ret += "\n\n\n"
    ret += "Informatii despre retea:\n"
    ret += "\nRUTE:\n" + network.gaseste_rute() + "\n"
    
    ret += "\nAdrese IP:\n" + network.gaseste_adrese() + "\n"

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
    ret += linux.gaseste_versiune_linux()
    ret += "</pre>"
    return ret
    
@app.route("/mem", methods=['GET'])
def info_memorie():
    ret = ""
    ret += f"<a href={url_for('index')}>acasa</a>"
    ret += "<pre>"
    ret += linux.gaseste_informatii_memorie(formatare = 1)
    ret += "</pre>"
    return ret
    
@app.route("/cpu", methods=['GET'])
def info_cpu():
    ret = ""
    ret += f"<a href={url_for('index')}>acasa</a>"
    ret += "<pre>"
    ret += linux.gaseste_informatii_cpu()
    ret += "</pre>"
    return ret

@app.route("/retea/rute", methods=['GET'])
def info_retea_rute():
    ret = ""
    ret += f"<a href={url_for('index')}>acasa</a>"
    ret += "<pre>"
    ret += str(network.gaseste_rute())
    ret += "</pre>"
    return ret


@app.route("/retea/adrese", methods=['GET'])
def info_retea_adrese():
    ret = ""
    ret += f"<a href={url_for('index')}>acasa</a>"
    ret += "<pre>"
    ret += str(network.gaseste_adrese())
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
    
    ret += f'<img src={url_for("static", filename="imagini/afisare_cu_punct.png")}>' + "<br/>"
    ret += f'<img src={url_for("static", filename="imagini/afisare_cu_steluta.png")}>' + "<br/>"
    ret += f'<img src={url_for("static", filename="imagini/afisare_cu_x.png")}>' + "<br/>"
    ret += f'<img src={url_for("static", filename="imagini/grafic_continuu_v1.png")}>' + "<br/>"
    ret += f'<img src={url_for("static", filename="imagini/grafic_continuu_v2.png")}>' + "<br/>"
    
    return ret
    
    
@app.cli.command()
def test():
    """
    Rulare 'unit tests'
    
    Apelare pytest din aplicatia systest, cu ajutorul comenzii flask.
    
    """
    import pytest
    sys.exit(pytest.main(["."]))
