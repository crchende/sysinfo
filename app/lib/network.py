import subprocess
import re

def gaseste_rute():
    '''
    Functie gaseste_rutele:

    OS suportat: Linux
    Verificat pe Ubuntu 20.04

    Se executa comanda route -n si se preia rezultatul.

    parametrii: -

    return: lista de dictionare
            pentru fiecare ruta se creeaza un dictionar cu cheile de mai sus    
    '''
    ret = []

    out_bin = subprocess.run(['route', '-n'], capture_output=True).stdout
    out_asc = out_bin.decode('ascii')
    
    return out_asc
    
    
def gaseste_linkuri():
    '''
    Functie: gaseste_linkuri:

    OS suportat: Linux
    Verificat pe Ubuntu 20.04

    Se executa comanda 'ip link' si se preia rezultatul.

    parametrii: -

    return: lista de dictionare
            pentru fiecare link se creeaza un dictionar cu chei - numele 
            parametrilor link-ului din ip link si valori - valorile acestor 
            parametrii.  
    '''
    ret = []

    try:
        out_bnr = subprocess.run(['ip', 'link'], capture_output=True).stdout
        out_str = out_bnr.decode('ascii').strip()
    
    except Exception as e:
        out_str = "EROARE executie comanda: 'ip link': " + str(e)
 
    return out_str


def gaseste_adrese():
    '''
    Functie gaseste_adrese:

    OS suportat: Linux
    Verificat pe Ubuntu 20.04

    Se executa comanda 'ip address' si se preia rezultatul.

    parametrii: -

    return: lista de dictionare
            pentru fiecare adresa se creeaza un dictionar cu chei
            numele parametrilor din comanda ip address si cu valori, valorile
            acestora.    
    '''  
    ret = []

    true = True

    try:
        out_bnr = subprocess.run(['ip', 'address'], capture_output=True).stdout
        out_str = out_bnr.decode('ascii').strip()
        
    except Exception as e:
        #print("Eroare executie comanda: 'ip address': ", e)
        out_str = "Eroare executie comanda: 'ip address': " + str(e)
 
    #print("DBG:", out_lst)
    return out_str



