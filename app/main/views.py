from flask import url_for, render_template
from app.lib import linux, network
from app.grafice.exemplu_func_grad_2 import genereaza_grafice, valori_x, valori_y
from . import main

@main.route("/", methods=['GET'])
def index():

    info_de_afisat = []

    info_de_afisat.append(v_os := linux.gaseste_versiune_linux())
    info_de_afisat.append(mem := linux.gaseste_informatii_memorie(formatare = 1))
    info_de_afisat.append(cpu := linux.gaseste_informatii_cpu())
    info_de_afisat.append(net_rute := network.gaseste_rute())
    info_de_afisat.append(net_adrese := network.gaseste_adrese())

    #print("DBG:" info_de_afisat)

    return render_template('index.html', info_de_afisat = info_de_afisat)

@main.route("/vos", methods=['GET'])
def versiune_os():
    info_de_afisat = []
    info_de_afisat.append(os := linux.gaseste_versiune_linux())
    return render_template('index.html', info_de_afisat = info_de_afisat)

    
@main.route("/mem", methods=['GET'])
def info_memorie():
    info_de_afisat = []
    info_de_afisat.append(mem := linux.gaseste_informatii_memorie(formatare = 1))
    #print("DBG: mem", info_de_afisat)
    return render_template('index.html', info_de_afisat = info_de_afisat)

    
@main.route("/cpu", methods=['GET'])
def info_cpu():
    info_de_afisat = []
    info_de_afisat.append(cpu:= linux.gaseste_informatii_cpu())
    return render_template('index.html', info_de_afisat = info_de_afisat)

@main.route("/retea/rute", methods=['GET'])
def info_retea_rute():
    info_de_afisat = []
    info_de_afisat.append(rute := str(network.gaseste_rute()))
    return render_template('index.html', info_de_afisat = info_de_afisat)


@main.route("/retea/adrese", methods=['GET'])
def info_retea_adrese():
    info_de_afisat = []
    info_de_afisat.append(adrese := str(network.gaseste_adrese()))
    return render_template('index.html', info_de_afisat = info_de_afisat)

@main.route("/grafic_x_patrat", methods=['GET'])
def grafic_x_patrat():
    info_de_afisat = []
    grafice = []
    genereaza_grafice(valori_x, valori_y, "app/static/imagini")

    info_de_afisat.append(f"valori x: {str(valori_x)}")
    info_de_afisat.append(f"valori y: {str(valori_y)}")
    
    grafice.append(url_for("static", filename="imagini/afisare_cu_punct.png"))
    grafice.append(url_for("static", filename="imagini/afisare_cu_steluta.png"))
    grafice.append(url_for("static", filename="imagini/afisare_cu_x.png"))
    grafice.append(url_for("static", filename="imagini/grafic_continuu_v1.png"))
    grafice.append(url_for("static", filename="imagini/grafic_continuu_v2.png"))

    #print("DBG: grafice:", grafice)

    return render_template('index.html', info_de_afisat = info_de_afisat, grafice = grafice)
    