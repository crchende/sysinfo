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
    
    print("DBG:", v)
    return(v)
    

def gaseste_informatii_memorie():
    '''
    Informatiile despre memorie pot fi vizualizate cu 'free -h'
    
    parametrii: 
    
    return:     o lista
    '''
    
    b_i = subprocess.run(['free', '-h'], capture_output = True).stdout
    i = b_i.decode('ascii').strip()
    
    
    
    print("DBG:", i)
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
    
    print("DBG:", i)
    return(i)
    
