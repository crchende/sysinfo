Acest director va contine imaginile generate cu matplotlib.
Exeplu folosit:

Functie de gratul 2: 
* y = x*x

Pentru x in {-10, -9, -8 ... 9, 10}

A se vedea in program cum sunt generate diverse grafice:
 - puncte - afisate cu diverse caractere si culori
 - linie obtinuta prin unirea punctelor, la fel poate afisata cu diverse culori
 - grafic cu titlu si etichata pentru x si y

Observatie.
Apelul plot.close() este necesar la utilizarea ca biblioteca.
Altfel desenele generate de plot vor fi suprapuse.
Daca se doreste sa avem suprapunere - de exemplu graficul in varianta continua peste care sa avem puncte, 
nu trebuie apelata metoda close intre cele 2 actiuni.
