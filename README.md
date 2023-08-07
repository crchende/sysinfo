# sysinfo

## v0.02 - afisare 'raw' fara formatare. Adaugare link-uri intre pagini si modul generare si afisare grafice.
* ruta standard '/' -> URL: http://127.0.0.1:5011
* rute in aplicatia WEB pentru:
  * versiune ubuntu: '/vos' -> URL: http://127.0.0.1:5011/vos,
  * memorie:         '/mem' ->                        .../mem
  * cpu:             '/cpu' ->                        .../cpu
  * rute retea:      'retea/rute'      -> URL: 'http://127.0.0.1:5011/retea/rute'
  * retea/interfete: 'retea/interfete' -> URL: 'http://127.0.0.1:5011/retea/interfete'

## Testare cu pytest
O parte din functiile din biblioteca de functii a aplicatie:
* directorul lib, fisierele:
  * ubuntu.py
  * network.py
au teste de tip 'unit - test' asociate - adica - este apelata functia si se asteapta o anumita valoare.
Testul compara valoarea obtinuta la apelul functie cu valoarea asteptata si returneaza PASS daca valoarea primita de la functie este cea asteptata si FAIL in caz contrar.

Pentru testare s-a folosit pachetul **pytest** din python. Acesta se afla in lista de pachete care trebuie instalate, in fisierul quickrequirements.txt

## Testare calitate cod
* **pylint** - pachet python folosit la testarea calitatii codului (spatii, nume variabile, variabile neutilizate etc.)
* in cazul de fata, problemele returnate de pylint doar sunt afisate, nu sunt considerate erori

Configurare .venv si instalare pachete:
---------------------------------------

In directorul 'app' rulati comenzile:

1) activeaza_venv: Incearca sa activeze venv-ul. 
                   Daca nu poate, configureaza venv-ul in directorul .venv si apoi instaleaza flask si flask-bootstrap.
                   La urmatoarea rulare, va activa doar venv-ul.
                
2) ruleaza_aplicatia: De rulat doar dupa activarea venv-ului. 
                      Va porni serverul pe IP: 127.0.0.1 si port: 5011.
                      Acces server din browser: http://127.0.0.1:5011

EXEMPLU activare venv si rulare:
---------------------------------------
    cip@cip:sysinfo$ source activeaza_venv 
    SUCCESS: venv was activated.
    
    (.venv) cip@cip:sysinfo$ source ruleaza_aplicatia 
    sysinfo
    WARNING: rand 6 []
     * Serving Flask app 'sysinfo'
     * Debug mode: off
    WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
     * Running on http://127.0.0.1:5011
    Press CTRL+C to quit
     * Restarting with stat
    sysinfo

![image](https://user-images.githubusercontent.com/57460107/222927371-97c8c4b9-37c0-4d1f-b6ab-c2f3851c77f7.png)


EXEMPLU pagina web - versiunea v0.02 - 
---------------------------------------
![image](https://github.com/crchende/sysinfo/assets/57460107/97f4c5ff-1c12-4ec6-8334-ad1950d8f664)

## Exemplu vizualizare versiune ubuntu:
![image](https://github.com/crchende/sysinfo/assets/57460107/0316f339-a277-4418-a1b0-d8ec0f022472)

## Exemplu pipeline Jenkins (conform fisierului Jenkins din repository-ul sysinfo)
![image](https://github.com/crchende/sysinfo/assets/57460107/8fdaa372-44ee-409b-855c-053e78baf800)

