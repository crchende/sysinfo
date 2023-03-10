import subprocess

def gaseste_versiune_ubuntu():
    '''
    Versiunea de ubuntu poate fi vazuta cu comenzile:
    cat /etc/issue
    lsb_release -d
    
    parametrii: -
    
    return:     versiunea de linux, fara eticheta 'Description:'
    '''
    
    b_v = subprocess.run(['lsb_release', '-d'], capture_output = True).stdout
    v = b_v.decode('ascii').strip()
    
    v = v.split(":")[1].strip()
    
    #print("DBG:", v)
    return(v)
    

def gaseste_informatii_memorie(formatare=0):
    '''
    Informatiile despre memorie pot fi vizualizate cu 'free -h'
    
    parametrii: 
    
    return:     o lista
    '''
    
    b_i = subprocess.run(['free', '-h'], capture_output = True).stdout
    i = b_i.decode('ascii')
    
    if formatare ==  1:
        frmt = "{:7}{:7}{:7}{:7}{:7}{:12}{:8}"

        linii = i.split('\n')
        
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
        
        i = frmt.format(*cap_tabel)
        sep = '-' * len(i)
        i += '\n' + sep + '\n'
 
        for m in (ram, swap):
            ln = frmt.format(*m)
            i += ln + "\n"

        return i

    #print("DBG:", i)
    return(i)
    

def gaseste_informatii_cpu():
    '''
    Informatiile despre memorie pot fi vizualizate cu 'cat /proc/cpuinfo | grep name'
    
    parametrii: 
    
    return:     o lista
    '''
    
    c_i = subprocess.run(['cat', '/proc/cpuinfo'], capture_output = True)
    b_i = subprocess.run(['grep', 'name'], capture_output = True, \
        input = c_i.stdout).stdout
        
    i = b_i.decode('ascii').strip()
    
    #print("DBG:", i)
    return(i)
    
