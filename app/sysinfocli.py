import app.lib.network as network
import app.lib.ubuntu as ubuntu

def creaza_meniu_principal():
    '''
    Creaza meniul principal.
    Din acesta, in functie de optiunea aleasa se va trece in submeniuri.
    Daca optiunea aleasa este 'x', nu se alega nici un meniu si se iese
    din functie.
    '''
    print("\n===========================")
    print("Meniu principal:")
    print("===========================")
    print("r  Configuratia de retelistica a calculatorului")
    print("s  Sistemul de operare (suport doar pentru UBUNTU)")
    print("Tasati:")
    print("x  pentru a iesi din program\n")
    
    c = input("Tastati optiunea: r / s / x: ")

    while c != 'r' and c != 's' and c != 'x':
        print("Optinue invalida:", c, "\n")
        c = input("Tastati optiunea: r / s / x: ")

    if c == "r":
        while creaza_meniu_retelistica() != 'x':
            pass
        
    elif c == 's':
        while creaza_meniu_sistem_operare() != 'x':
            pass

    return c


def creaza_meniu_sistem_operare():
    mesaje = ["-------------------------------",
              "Meniu Sistem Operare (Ubuntu):",
              "-------------------------------",
              "v  Versiune OS",
              "c  CPU",
              "m  Memorie"
              "Tastati:",
              "x  pentru a reveni in meniul principal"]
    mesaj_input = "Tastati optiunea: v / c / m / x: "
    
    #afisare meniu
    print("")
    for m in mesaje:
        print(m)
    
    c = input(mesaj_input)
    
    while(c != 'v' and c != 'c' and c != 'm' and c != 'x'):
        print("Optiune invalida: ", c, "\n")
        c = input(mesaj_input)

    i = "NA"
    if c == 'v':
        i = ubuntu.gaseste_versiune_ubuntu()
    elif c == 'c':
        i = ubuntu.gaseste_informatii_cpu()        
    elif c == 'm':
        i = ubuntu.gaseste_informatii_memorie(formatare = 1)

    if i != "NA":
        print(f'\n{i}\n')
        
    #necesar pentru a iesi din bucla din meniul principal
    return c


def creaza_meniu_retelistica():
    mesaje = ["-------------------------------",
              "Meniu Retelistica:",
              "-------------------------------",
              "!!! In constructie. Tastati:",
              "x  pentru a reveni in meniul principal"]
    mesaj_input = "Tastati optiunea: x: "
    
    #afisare meniu
    print("")
    for m in mesaje:
        print(m)
    
    c = input(mesaj_input)
    
    while(c != 'x'):
        print("Optiune invalida: ", c, "\n")
        c = input(mesaj_input)

    #necesar pentru a iesi din bucla din meniul principal
    return c

#print(__name__)
if __name__ == "__main__":
    while creaza_meniu_principal() != 'x':
        pass