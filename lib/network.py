import subprocess
import re


def gaseste_rutele():
    '''
    OS suportat: Linux
    Verificat pe Ubuntu 20.04
    
    Se executa comanda route -n si se preia rezultatul.
    Din text-ul rezultat se creaza o lista de dictionare. 
    Numarul de elemente din lista va fi egal cu numarul de rute.
    Pentru fiecare ruta, avem un dictionar cu chei date de parametrii rutei:
        - Destination
        - Gateway
        - Genmask
        - Flags
        - Metric
        - Ref
        - Use
        - Iface 
    
    parametrii: -
    
    return: lista de dictionare
            pentru fiecare ruta se creeaza un dictionar cu cheile de mai sus    
    '''
    
    ret = []

    out_bin = subprocess.run(['route', '-n'], capture_output=True).stdout
    out_asc = out_bin.decode('ascii')
    
    # procesare text returnat de comanda 'route -n'
    out_lst = out_asc.split("\n")
    
    lst_chei = out_lst[1].split()
    #print("DBG:", lst_chei)

    for i in range(2, len(out_lst)):
        #print("DBG:", out_lst[i])
        d = {}
        lst_rand = out_lst[i].split()
        if len(lst_rand) < len(lst_chei):
            print("WARNING: rand", i, lst_rand)
            continue
        else:
            pass
            #print("DBG:", lst_rand)
        for j in range(0, len(lst_chei)):
            #print(lst_chei[j], lst_rand[j])
            d[lst_chei[j]] =  lst_rand[j]
        
        ret.append(d)

    #print("DBG:", ret)
    return ret
    

def gaseste_linkuri():
    '''
    OS suportat: Linux
    Verificat pe Ubuntu 20.04
    
    Se executa comanda 'ip link' si se preia rezultatul.
    Din text-ul rezultat se creaza o lista de dictionare. 
    Numarul de elemente din lista va fi egal cu numarul de interfete.
    Pentru fiecare interfata, vom avea in lista un dictionar cu parametrii si 
    valorile pentru fiecare parametru.
    
    parametrii: -
    
    return: lista de dictionare
            pentru fiecare link se creeaza un dictionar cu chei - numele 
            parametrilor link-ului din ip link si valori - valorile acestor 
            parametrii.  
    '''    

    ret = []

    out_bnr = subprocess.run(['ip', '-j', 'link'], capture_output=True).stdout
    out_str = out_bnr.decode('ascii').strip()
    
    out_lst = eval(out_str)
 
    #print(out_lst)
    return out_lst
    
def gaseste_adrese():
    '''
    OS suportat: Linux
    Verificat pe Ubuntu 20.04
    
    Se executa comanda 'ip -j address' si se preia rezultatul.
    Din text-ul rezultat se creaza o lista de dictionare. 
    Numarul de elemente din lista va fi egal cu numarul de interfete.
    Pentru fiecare interfata, vom avea in lista un dictionar cu parametrii si 
    valorile pentru fiecare parametru.
    
    parametrii: -
    
    return: lista de dictionare
            pentru fiecare adresa se creeaza un dictionar cu chei
            numele parametrilor din comanda ip address si cu valori, valorile
            acestora.    
    '''    

    ret = []

    true = True

    out_bnr = subprocess.run(['ip', '-j', 'address'], capture_output=True).stdout
    out_str = out_bnr.decode('ascii').strip()
    
    out_lst = eval(out_str)
 
    #print("DBG:", out_lst)
    return out_lst
    
    
def genereaza_tabela_rute(rute, *param):
    ret = []
    chei = rute[0].keys()
    
    l_param = []
    
    if param == ():
        l_param = ["Destination", "Gateway", "Genmask", "Iface"]
    elif param == ("all"):
        l_param = list(chei)
        
    ret.append(l_param)
            
    for r in rute:
        r_lst = []
        for c in l_param:
            r_lst.append(r[c])

        #print("DBG:", r_lst)
        ret.append(r_lst)
        
    #print("DBG:", ret)
    return ret    
        
    
