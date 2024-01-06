import matplotlib
import matplotlib.pyplot as plt
import os

if __name__ != "__main__":
    matplotlib.use("agg")
# Generare seturi de date cu list comprehension
valori_x = [a for a in range(-10, 10+1)]
valori_y = [a*a for a in valori_x]


'''
    Functie care genereaza grafice pentru o functie de grad 2, avand dat setul de valori pentru x si y
    
    Parametrii:
        x: setul de valori pentru axa Ox
        y: setul de valori pentru axa Oy
        locatie_imagini: locul unde vor fi salvate imaginile
        
'''
def genereaza_grafice(x, y, locatie_imagini):
    cale_dir_curent = os.path.abspath(os.path.curdir)
    print("DBG: director salvare imagini:", locatie_imagini)    
    print("DBG: director curent:", cale_dir_curent)
    locatie_imagini = os.path.join(cale_dir_curent, locatie_imagini)
    
    #############################
    # afisare cu puncte
    ##############################
    # fara parametrul marker, se afiseaza puncte, altfel, se afiseaza caracterul dat ca parametru
    fig1 = plt.scatter(x, y, c='red', marker='x')
    print("afisare obiect fig1 (reprezentarea interna, nu imagine)", fig1, type(fig1))
    # salvare sub forma de jpg
    if __name__ == "__main__":
        print("**************************************")
        plt.show() # de comentat daca nu vrem sa se intrerupa executia si sa se afiseze graficul
    fig1.figure.savefig(os.path.join(locatie_imagini, 'afisare_cu_x.png'))
    plt.close()

    # alta reprezentare a aceluiasi set de date - culoare + forma punct
    fig2 = plt.scatter(x, y, c='blue', marker='*')
    print("afisare obiect fig1 (reprezentarea interna, nu imagine)", fig2, type(fig2))
    # salvare sub forma de jpg
    if __name__ == "__main__":
        plt.show() # de comentat ...
    fig2.figure.savefig(os.path.join(locatie_imagini, 'afisare_cu_steluta.png'))
    plt.close()

    # alta reprezentare a aceluiasi set de date - culoare + forma punct
    fig3 = plt.scatter(x, y, c='green')
    print("afisare obiect fig1 (reprezentarea interna, nu imagine)", fig3, type(fig3))
    # salvare sub forma de jpg
    if __name__ == "__main__":
        plt.show() # de comentat ...
    fig3.figure.savefig(os.path.join(locatie_imagini, 'afisare_cu_punct.png'))
    plt.close()

    ##############################
    # afisare linie contiuna
    ##############################
    # spre deosebire de scatter, plot genereaza un alt tip de obiect care nu este de tip figura
    ob_1 = plt.plot(x, y)
    print(ob_1, type(ob_1))
    if __name__ == "__main__":
        plt.show()

    # apel metoda savefig pentru a salva imaginea intr-un fisier
    plt.savefig(os.path.join(locatie_imagini, 'grafic_continuu_v1.png'))
    plt.close()
    
    # adaugare etichete axe + titlu dar trebuie regenerat graficul ...
    ob_2 = plt.plot(x, y)
    print(ob_2, type(ob_2))
    plt.title(f"{locatie_imagini}/functia de grad 2")
    plt.xlabel("X")
    plt.ylabel("X*X")
    if __name__ == "__main__":
        plt.show()
    plt.savefig(os.path.join(locatie_imagini, 'grafic_continuu_v2.png'))
    plt.close()

    # functia doar genereaza grafice.
    # am putea returna 1 pentru a sti ca s-a ajuns la sfarsit si nu au aparut erori
    return 1


# Executie functie daca incercam sa executam fisierul, nu sa-l folosim ca librarie
# Cand este folosit ca librarie, n-am vrea sa si executam functia.
# Acest lucru va fi facut de programul care foloseste libraria
if __name__ == "__main__":
    genereaza_grafice(valori_x, valori_y, "../../static/imagini")
    



