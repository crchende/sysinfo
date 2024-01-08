import subprocess

def gaseste_versiune_linux():
    '''
    Versiunea de ubuntu poate fi vazuta cu comenzile:
    cat /etc/issue
    lsb_release -d
    (cat /etc/os-release)
    
    lsb_release - posibil as nu mearga pe toate versiunile de linux
    si nu merge in docker
    In caz de eroare se incearca preluarea informatiilor despre sistemul 
    de operare din /etc/issue.
    
    parametrii: -
    
    return:     versiunea de linux, fara eticheta 'Description:'
    '''
    
    v = ""
    
    # tratare eroare apel 'lsb_release -b'
    try:
        b_v = subprocess.run(['lsb_release', '-d'], capture_output = True).stdout
        v = b_v.decode('ascii').strip()
    
        v = v.split(":")[1].strip()
    except Exception as e:
        print("Eroare executie comanda: 'lsb_release -d': ", e)
        v = "Eroare executie comenzii: 'lsb_release -d'"
        try:
            b_v = subprocess.run(['cat', '/etc/issue'], capture_output = True).stdout
            v = b_v.decode('ascii').strip()
        except Exception as e:
            print("Eroare si la executia comenzii: 'cat /etc/issue':", e)
            v = "Eroare si la executia comenzii: 'cat /etc/issue'"

    #print("DBG:", v)
    return(v)
    

def gaseste_informatii_memorie(formatare=0):
    '''
    Informatiile despre memorie pot fi vizualizate cu 'free -h'
    
    Daca functia este apelata cu valoarea 1 sau explicit 'formatare = 1' rezultatul
    comenzii care afiseaza memoria este preluat si formatat conform specificatiei
    de formatare din variabila 'frmt'.
    Intre capul de tabel si date se adauga o linie.
    
    parametrii: formatare, cu valoarea implicita 0 - se returneaza datele neformatate
    
    return:     o lista
    '''
    
    b_i = subprocess.run(['free', '-h'], capture_output = True).stdout
    ret = b_i.decode('ascii')
    
    #formatare 'ret' daca functia este apelata cu parametrul formatare = 1
    if formatare ==  1:
        frmt = "{:7}{:>8}{:>7}{:>7}{:>7}{:>14}{:>12}"

        linii = ret.split('\n')
        
        cap_tabel = linii[0].split()    
        ram = linii[1].split()
        swap = linii[2].split()

        #normalizare output
        #din cap tabel lipseste primul element - tipul de memorie
        cap_tabel.insert(0,'')
        l = len(cap_tabel)

        #luam celelalte linii si le aducem la lungimea capului de tabel

        for m in (ram, swap):
            l_m = len(m)
            for i in range(l_m, l):
                m.append("")
                
        #print("DBG", len(cap_tabel), len(ram), len(swap))
        
        ret = frmt.format(*cap_tabel)
        sep = '-' * len(ret)
        ret += '\n' + sep + '\n'
 
        for m in (ram, swap):
            ln = frmt.format(*m)
            ret += ln + "\n"

    return ret
    

def gaseste_informatii_cpu():
    '''
    Informatiile despre memorie pot fi vizualizate cu 'cat /proc/cpuinfo | grep name'
    
    parametrii: 
    
    return:     o lista
    '''
    
    c_i = subprocess.run(['cat', '/proc/cpuinfo'], capture_output = True)
    b_i = subprocess.run(['grep', 'name'], capture_output = True, \
        input = c_i.stdout).stdout
    
    #Stergere caractere albe (spatii, tab) de la inceput si de la sfarsit - strip()    
    i = b_i.decode('ascii').strip()
    
    #print("DBG:", i)
    return(i)
    
